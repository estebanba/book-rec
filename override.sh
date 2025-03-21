#!/bin/bash

# This script runs before the app starts in Streamlit Cloud

# Create the constraints file
echo "# Explicitly exclude the Apple-specific package" > constraints.txt
echo "thinc-apple-ops==0.0.0" >> constraints.txt

# Install dependencies with constraints
pip install -U pip
pip install -c constraints.txt -e .

# Download spaCy model directly if needed
python -m spacy download en_core_web_sm --no-deps

# Print installed packages for debugging
pip list
