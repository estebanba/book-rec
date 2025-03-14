# Building Permits X-Ray: Cambridge, MA

![Building Permits Dashboard](images/dashboard_screenshot.png)

## Project Overview

This data analytics project analyzes building permit data from the City of Cambridge's Open Data Program to understand how construction factors affect building permit amounts and costs. The analysis provides valuable insights for city authorities, real estate companies, construction firms, and related businesses.

## Table of Contents

- [Project Description](#project-description)
- [Data Source](#data-source)
- [Key Questions](#key-questions)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Key Findings](#key-findings)
- [Recommendations](#recommendations)
- [Dashboard](#dashboard)
- [Limitations and Future Work](#limitations-and-future-work)
- [Setup and Installation](#setup-and-installation)

## Project Description

Building permits are official approvals to construct new buildings or modify existing ones. This project analyzes permit data to understand trends, patterns, and factors that influence construction costs and permit issuance in Cambridge, MA.

The project follows a complete data analysis pipeline including data collection, cleaning, exploration, analysis, and visualization, culminating in interactive dashboards for decision-making.

## Data Source

- **City of Cambridge - Open Data Program**
- Primary dataset: [Building Permits: Addition/Alteration](https://data.cambridgema.gov/Inspectional-Services/Building-Permits-Addition-Alteration/qu2z-8suj/about_data)
- The dataset contains approximately 11,000 building permit records spanning 7 years (2018-2025)
- Data includes various building uses, construction types, and involves around 2,500 companies

## Key Questions

- How has the development of permitting evolved in recent years?
- Do seasons affect the number of permits issued in a year?
- How do different factors affect construction costs? 
- Are there months/seasons when costs are higher than others?
- What patterns exist across different building types and construction methods?

## Technologies Used

- **Python** for data cleaning, processing, and analysis
- **Pandas, NumPy** for data manipulation
- **Matplotlib, Seaborn** for data visualization
- **SQL** for database queries and analysis
- **Tableau** for interactive dashboards and visualization

## Project Structure

```
data-bootcamp-final-project/
├── data/                   # Raw and processed data files
│   ├── raw/                # Original dataset files
│   └── clean/              # Cleaned and transformed datasets
│   └── scripts/            # SQL scripts for database creation and queries
├── notebooks/              # Jupyter notebooks for analysis
│   ├── cleaning_building_permits.ipynb
│   ├── seeding_building_permits.ipynb
│   ├── analysis_building_permits.ipynb
│   ├── hypothesis_building_permits.ipynb
│   ├── functions.py
│   └── firm_name_cleaner.py
├── README.md               # Project description and documentation
└── requirements.txt        # Required Python packages
```

## Key Findings

- **Permit Issuance Trends**: No significant differences in number of permits year over year, with a slight decrease during COVID-19.
- **Seasonal Effects**: Permits issued in February and October have the lowest average total cost.
- **Construction Types**: Wood construction leads in both number of permits and costs.
- **Building Use Cost Discrepancy**: Commercial and mixed-use buildings show a strong imbalance in average total cost compared to residential buildings.
- **Unit Count Impact**: Buildings with 6 units cost more on average, while buildings with 9-10 units present lower costs.
- **Cost Factors**: All amenities and extras increase the total cost, with the exception of including a condominium association.
- **Seasonal Construction**: Seasons slightly affect exterior works, with spring showing the highest percentage of exterior change permits.

## Recommendations

- Aim to have permits issued before February or October for potentially lower costs.
- Focus on buildings with 9 or 10 units and avoid buildings with 6 units when possible.
- Consider forming a condominium association, which correlates with lower costs.
- For commercial and mixed-use buildings, pay special attention to subsystems costs, which form a significant portion of the total cost.

## Dashboard

The project includes interactive Tableau dashboards that allow users to:
- Explore building permit trends over time
- Analyze costs by building type, construction method, and season
- Visualize geographical distribution of permits
- Examine contractor performance and prevalence
- Filter data by various dimensions for customized views

## Limitations and Future Work

- **Limitations**: 
  - Survivor bias in the data (only approved permits are included)
  - No information about rejected permit applications
  - Limited to Cambridge, MA area

- **Future Work**:
  - Further geographical analysis to identify neighborhood-specific patterns
  - Integration with other municipal datasets for broader context
  - Predictive modeling for construction costs
  - Comparative analysis with other similar-sized cities

## Setup and Installation

1. Clone this repository:
```
git clone https://github.com/estebanba/data-bootcamp-final-project.git
cd data-bootcamp-final-project
```

2. Install required packages:
```
pip install -r requirements.txt

# or if using uv

uv pip install -r requirements.txt
```

3. Run the notebooks in the following order:
  - cleaning_building_permits.ipynb
  - analysis_building_permits.ipynb

4. [Click here to open the Tableau dashboards in the tableau directory for interactive exploration](https://public.tableau.com/app/profile/esteban.basili/viz/DA_final_project_17419449525070/Costs?publish=yes)
