# Analyzing-Crime-Data-in-Washington-DC
Data-driven analysis of ~300K Washington D.C. crime records using Python/R to uncover spatial hotspots, temporal trends, and actionable insights for improved resource allocation.


# Crime Data Analysis in Washington, D.C.

This project analyzes crime incidents in Washington, D.C. to identify spatial and temporal patterns, detect hotspots near key landmarks, and generate insights for better resource allocation and public safety strategies.

## Project Overview

- Analyzed ~300K crime records from Washington, D.C.
- Focused on:
  - Spatial patterns (location, proximity to landmarks)
  - Temporal patterns (time of day, day of week)
  - Incident categories and trends over time
- Used geospatial analysis to identify crime hotspots and support data-informed patrol planning.

## Tech Stack

- **Languages:** Python, R
- **Python:** pandas, numpy, matplotlib / seaborn (and any others you used)
- **R:** tidyverse, ggplot2, etc. (from the R Markdown)
- **Data:** D.C. crime incident dataset (`dc_crime_data.csv`)

## Repository Structure

```text
dc-crime-analysis/
│── README.md
│── data/
│   └── dc_crime_data.csv
│── src/
│   └── crime_analysis.py
│── notebooks/
│   └── crime_analysis.Rmd
│── reports/
│   ├── DC_Crime_Analysis_Report.pdf
│   └── DC_Crime_R_Output.pdf
│── visuals/
│   └── hotspot_map.png (example)
│── requirements.txt
└── LICENSE
