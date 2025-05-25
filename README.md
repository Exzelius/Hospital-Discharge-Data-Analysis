# Hospital Discharge Data Analysis (SPARCS 2021, NYSDOH)

This project analyzes the 2021 New York State SPARCS inpatient discharge dataset to uncover trends in diagnoses, severity, mortality risk, and outcomes. The workflow demonstrates robust data cleaning, transformation, exploratory analysis, and interactive visualization.


## Features

- Cleans and standardizes patient-level hospital discharge data
- Engineers features for severity, payment type, and outcomes
- Explores trends by age group, diagnosis, and discharge disposition
- Visualizes key metrics (admissions, severity, LOS, mortality risk) using Python (matplotlib, seaborn)
- Outputs ready-to-use, cleaned CSV for further analytics or dashboarding

## Setup

1. Clone this repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Place `hospital_data.csv` in the `data/` directory.

## Usage

Open and run the Jupyter notebook:
```
jupyter notebook Analysis.ipynb
```
or use VS Code with the Jupyter extension.

## Outputs

- Cleaned data: `data/hospital_data_cleaned.csv`
- Visualizations: admissions by age/severity, top diagnoses, mortality risk heatmap, LOS by disposition

## Results

- Identified top 10 DRGs by admission count
- Quantified LOS and severity trends across age groups
- Provided actionable insights for hospital resource planning

## License

MIT License