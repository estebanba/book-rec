# firm_name_cleaner.py
# A script to clean and standardize firm names in a pandas DataFrame

# Import necessary libraries
import re
from collections import defaultdict
import pandas as pd
import spacy
from thefuzz import fuzz, process

# Load SpaCy model - using the Apple-compatible version
try:
    nlp = spacy.load("en_core_web_sm")
except:
    # In case the model isn't installed yet
    print("You may need to install the spaCy model first with: python -m spacy download en_core_web_sm")

def basic_clean(text):
    """Basic text cleaning operations"""
    # Convert to string and handle None values
    text = str(text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Note: We are NOT removing suffixes like "inc", "llc", "corp", etc.
    # per user request
    
    # Remove punctuation except for characters that might be part of names
    # but preserve dots in abbreviations like "Inc." or "L.L.C."
    text = re.sub(r'[^\w\s\-&\.]', '', text)
    
    # Replace consecutive spaces with a single space
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text.strip()

def normalize_for_grouping(text):
    """Aggressively normalize text for grouping similar company names"""
    # Convert to lowercase
    text = str(text).lower()
    
    # Remove all punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # Replace spaces between single letters with nothing (j b -> jb)
    text = re.sub(r'\b(\w)\s+(\w)\b', r'\1\2', text)
    
    # Remove all titles and common words that don't help differentiate
    text = re.sub(r'\b(inc|incorporated|llc|ltd|limited|corp|corporation|company|co|construction|contracting|contractors|enterprises|group|associates|services|home|energy|llp|the|and|&|of|for|by|builder|builders|building|remodeling|renovations|windows|windows|properties|property)\b', ' ', text)
    
    # Remove very common short suffixes
    text = re.sub(r'\s+(inc|llc|ltd|co|corp)$', '', text)
    
    # Remove leading "the"
    text = re.sub(r'^the\s+', '', text)
    
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text.strip()

def standardize_names(names, min_similarity=75):
    """Group similar company names while selecting the most complete name as standard"""
    # First pass: sort by frequency and length
    name_counts = defaultdict(int)
    for name in names:
        name_counts[name] += 1
    
    # Sort names by frequency (most common first), then by length (longest first)
    sorted_names = sorted(name_counts.keys(), 
                         key=lambda x: (name_counts[x], len(x), x.count(' ')), 
                         reverse=True)
    
    # Create mapping of original names to standardized names
    name_mapping = {}
    reference_names = []
    reference_normalized = []
    
    # Process each name
    for name in sorted_names:
        # Skip empty strings
        if not name.strip() or name.strip().lower() in ['none', 'other', '.', 'na', 'n/a']:
            name_mapping[name] = name
            continue
        
        # Skip very short names that are likely abbreviations, unless frequent
        if len(name) < 3 and name_counts[name] < 3:
            name_mapping[name] = name
            continue
            
        # Normalize for grouping
        name_norm = normalize_for_grouping(name)
        
        # If normalized version is empty after removing common words, use a simpler normalization
        if not name_norm.strip():
            name_norm = name.lower().strip()
        
        # If this is our first name, add it as a reference
        if not reference_names:
            reference_names.append(name)
            reference_normalized.append(name_norm)
            name_mapping[name] = name
            continue
        
        # Try to find a match among existing references
        best_match = None
        best_score = 0
        best_index = -1
        
        # First try for exact matches after normalization
        exact_match_found = False
        for i, ref_norm in enumerate(reference_normalized):
            # If normalized versions match exactly
            if name_norm == ref_norm:
                best_match = reference_names[i]
                best_index = i
                best_score = 100
                exact_match_found = True
                break
        
        # If no exact match, try fuzzy matching
        if not exact_match_found:
            for i, ref_norm in enumerate(reference_normalized):
                # Try different matching algorithms
                token_sort_score = fuzz.token_sort_ratio(name_norm, ref_norm)
                ratio_score = fuzz.ratio(name_norm, ref_norm)
                
                # Use the higher of the two scores
                score = max(token_sort_score, ratio_score)
                
                # Add bonuses for certain conditions
                # Bonus if first word matches
                if len(name_norm.split()) > 0 and len(ref_norm.split()) > 0:
                    if name_norm.split()[0] == ref_norm.split()[0]:
                        score += 5
                
                # Bonus if one is contained completely in the other
                if name_norm in ref_norm or ref_norm in name_norm:
                    score += 5
                    
                if score > best_score and score >= min_similarity:
                    best_score = score
                    best_match = reference_names[i]
                    best_index = i
        
        # If we found a match
        if best_match:
            # Consider which name version to keep as the reference
            # Choose the longer, more complete name
            current_name_quality = len(name) + name.count(' ') * 2
            best_match_quality = len(best_match) + best_match.count(' ') * 2
            
            # If current name is better, update the reference
            if current_name_quality > best_match_quality:
                # Update all mappings to the old reference
                for key, value in list(name_mapping.items()):
                    if value == best_match:
                        name_mapping[key] = name
                
                # Update reference
                reference_names[best_index] = name
                reference_normalized[best_index] = name_norm
                name_mapping[name] = name
            else:
                name_mapping[name] = best_match
        else:
            # No match found, add as new reference
            reference_names.append(name)
            reference_normalized.append(name_norm)
            name_mapping[name] = name
            
    return name_mapping

def clean_firm_names(df, min_similarity=75, column_name='firm_name'):
    """
    Clean and standardize firm/company names in a DataFrame column
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame containing the firm names
    min_similarity : int, optional
        The minimum similarity threshold for grouping names (default: 75)
    column_name : str, optional
        The name of the column containing firm names to clean (default: 'firm_name')
        
    Returns:
    --------
    pandas.DataFrame
        DataFrame with cleaned firm names and original names
    """
    # Create a copy of the DataFrame to avoid modifying the original
    result_df = df.copy()
    
    # Create a copy of the original column
    result_df['original_firm_name'] = result_df[column_name].copy()
    
    # Basic cleaning (keeps original capitalization)
    result_df[column_name] = result_df[column_name].astype(str)
    result_df[column_name] = result_df[column_name].apply(lambda x: basic_clean(x))
    
    # Group similar names
    cleaned_names = standardize_names(result_df[column_name].tolist(), min_similarity)
    
    # Apply standardized names
    result_df['standardized_firm_name'] = result_df[column_name].map(cleaned_names)
    
    return result_df

# Example usage
if __name__ == "__main__":
    # Create sample data with variations of the same company
    data = {
        'firm_name': [
            'J B Sash & Door Company Inc',
            'J.B. SASH & DOOR COMPANY',
            'J.B. SASH AND DOORS',
            'JB Sash & Door Co',
            'J B SASH & DOOR',
            'Renewal by Andersen',
            'renewal by Andersen',
            'TC Remodeling',
            'T.C. Remodeling Inc',
            'Russell Remodeling',
            'Russell Remodeling LLC',
            'Russell Remodeling and Restoration',
            'Dan Han Construction',
            'Jason Du Construction Co.',
            'Metro Insulation, Inc',
            'Jones Boys Insulation',
            'Jones Boys Insulation Inc.',
            'The Jones Boys'
        ]
    }
    
    # Create a DataFrame
    sample_df = pd.DataFrame(data)
    
    # Clean the firm names with more aggressive matching
    cleaned_df = clean_firm_names(sample_df, min_similarity=75)
    
    # Display the results
    print(cleaned_df[['original_firm_name', 'firm_name', 'standardized_firm_name']])
    
    # Count unique standardized names
    unique_count = cleaned_df['standardized_firm_name'].nunique()
    original_count = len(data['firm_name'])
    
    print(f"\nReduced from {original_count} original names to {unique_count} standardized names")
    print(f"Reduction of {original_count - unique_count} names ({((original_count - unique_count) / original_count * 100):.1f}%)")