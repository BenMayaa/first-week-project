MoonLight Energy Solutions: Solar Radiation Analysis Project

Project Overview
This project was developed as part of the first week's assignment in the [Course Name] course. The objective was to analyze environmental measurement data provided by MoonLight Energy Solutions to identify key trends and insights that would inform strategic solar investments. The project focuses on Exploratory Data Analysis (EDA), statistical analysis, and the development of a Streamlit dashboard to visualize the insights gained.

Table of Contents
1. Project Structure
2. Setup Instructions
3. Data Understanding
4. Exploratory Data Analysis (EDA)
5. [Data Cleaning](#data-cleaning)
6. Streamlit Dashboard
7. Git and GitHub Workflow
8. Conclusion





Project Structure
The project follows a well-organized folder structure as outlined below:
moonlight-energy-analysis/
├── .vscode/
│   └── settings.json            
├── .github/
│   └── workflows/
│       ├── unittests.yml        
├── .gitignore                   
├── requirements.txt             
├── README.md                    
├── src/                         
├── notebooks/
│   ├── analysis.ipynb           
│   └── README.md                
├── tests/
│   ├── __init__.py              
├── scripts/
│   ├── __init__.py              
│   └── README.md                
├── app/
│   ├── main.py                  
│   ├── utils.py                 
└── data/
    └── solar_data.csv           
Setup Instructions
Prerequisites
- Python 3.x
- Git
- Virtual environment 
- Streamlit (for the dashboard)

Installation
1. Clone the Repository:
2. Create and Activate a Virtual Environment:
3. Install Dependencies:
4. Run the Jupyter Notebook:
5. Run the Streamlit Dashboard:

Data Understanding
The dataset used in this project was extracted from Solar Radiation Measurement Data. The data includes several columns representing various environmental factors such as solar radiation, air temperature, humidity, wind speed, and more. Each observation is timestamped, allowing for time-series analysis.





Exploratory Data Analysis (EDA)
Summary Statistics
The summary statistics provided an overview of the dataset, including measures such as mean, median, and standard deviation for key numeric columns.
Data Quality Checks
- Missing Values: 
Identified and filled missing values using forward fill techniques.
- Outliers: 
Detected using box plots and handled appropriately.

Time Series Analysis
- Trends: 
Analyzed patterns in solar radiation and temperature over time.
- Anomalies: 
Identified peaks in solar irradiance and temperature fluctuations.

Correlation Analysis
- Heatmaps: 
Visualized the correlations between different environmental factors.
- Key Insights:
Found strong correlations between certain solar radiation measures and temperature readings.



Wind and Temperature Analysis
- Polar Plots: 
Analyzed wind direction and speed (though simplified due to time constraints).
- Temperature vs. Humidity: 
Explored the relationship between ambient temperature and relative humidity.

Data Cleaning
Based on the initial analysis, the dataset was cleaned by:
- Handling Missing Values: 
Used forward fill to handle missing data in the time series.
- Removing Outliers: 
Capped or removed outliers in sensor readings and wind speed data.

Streamlit Dashboard
A Streamlit dashboard was developed to visualize the key insights gained from the EDA. The dashboard includes interactive features such as sliders and buttons to allow users to explore different aspects of the data.
Key Features:
- Time Series Visualization: 
Allows users to observe trends over time.
- Correlation Heatmap:
 Provides an interactive heatmap to explore correlations.
- Data Filtering: 
Users can filter the data based on various environmental factors.

Git and GitHub Workflow
Branching and Merging
- A new branch `task-1` was created for this task.
- All work was committed with descriptive messages to ensure a clear version history.
- After completing the task, the `task-1` branch was merged into the `main` branch using a Pull Request (PR).
Commit History:
- Initial Setup:
 "Initial project setup with folder structure and Python environment."
- EDA and Cleaning: 
"Completed initial EDA with summary statistics and data cleaning."
- Dashboard Development:
 "Developed Streamlit dashboard for data visualization."

Conclusion
This project successfully implemented the required tasks, including setting up a GitHub repository, performing EDA, cleaning the dataset, and developing a Streamlit dashboard. The insights gained from this analysis will help MoonLight Energy Solutions make data-driven decisions for their solar investment strategy.
The final analysis suggests focusing on regions with high solar irradiance (GHI, DNI) and stable environmental conditions (low wind variability, consistent temperatures) for optimal solar installation. Further analysis is recommended to refine these insights and align them with the company’s long-term sustainability goals.
