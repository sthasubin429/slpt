#  CPSC 4810 Group Project - Team Strong


## Table of Contents
- [Overview](#overview)
- [Team Members](#team-members)
- [Folder Structure](#folder-structure)
- [Installation](#installation)


## Overview
Group project for CPSC 4810.


## Team Members
- Luke Hyatt (<lhyatt@langara.ca>)
- Patcharapa Pinnarat (<ppinnarat00@mylangara.ca>)
- Subin Shrestha (<sshrestha10@mylangara.ca>)
- Thi Thu Thuy Tran (<ttran084@mylangara.ca>)

## Problem Statement
The objective of this project is to analyze telecom customer data to identify patterns and factors that contribute to customer churn. This will allow the company to take proactive steps to reduce churn and improve customer retentio

## Data Source
- Data Set Used: [Telecom Churn Dataset](https://www.kaggle.com/datasets/jpacse/datasets-for-churn-telecom) from Kaggle.
- Using cell2celltrain.csv file.


## Folder Structure
```
slpt/
├── data/                      # Contains datasets and raw data files
│   ├── raw/                   # Original data files
│   │   └── cell2celltrain.csv # Original dataset file
│   ├── interim/               # Intermediate data files
│   └── processed/             # Processed data files
├── src/                       # Source code for data processing and modeling
│   ├── dashboard/             # Dashboard files
├── requirements.txt           # Python dependencies
├── images/                    # Generated Images
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore file
```


## Installation
1. Clone the repository:
  ```code
  git clone gituser@ubuntu.mbouguerra.com:/opt/git-repos/slpt
  cd slpt
  ```

2. Create and activate a virtual environment:
  ```code
  python3 -m venv venv
  source venv/bin/activate
  ```

3. Install the required dependencies:
  ```code
  pip install -r requirements.txt
  ```

4. Use VSCode or Run the Jupyter Notebook:
  ```code
  jupyter notebook
  ```

## Running the Dashboard
To run the Streamlit dashboard, execute the following command from the project root directory:

```bash
streamlit run src/dashboard/app.py
```

Make sure your virtual environment is activated and all dependencies are installed. The dashboard will open in your default web browser.
A PDF version of the dashboard is also available in the `images` folder.
