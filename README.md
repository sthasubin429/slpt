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
├── notebooks/                 # Jupyter notebooks for analysis and modeling
├── src/                       # Source code for data processing and modeling
├── requirements.txt           # Python dependencies
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
