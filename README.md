# Data Cleaning Task

## Overview
This repository contains a Python script for cleaning and processing data from a CSV file. The script performs several operations, including removing duplicates, converting salary from USD to EGP, and calculating basic statistics.

## Requirements
- Python 3.x
- pandas library

## Installation
To run this script, you need to have Python and pip installed. You can install the required `pandas` library using:

```bash
pip install pandas

2-Usage
1-Place your CSV file in the same directory as the script. Rename it to your_file.csv or update the script to point to your file name.
2-Run the script using the following command:

python data_processing.py

3-The script will:
Load data from your_file.csv
Remove duplicates
Convert the Age column to integer values
Convert Salary(USD) to Salary_EGP (using a conversion rate of 30.85)
Calculate and print:
Average Age
Median Salary in EGP
Ratio of Males to Females
Save the modified data to modified_data.csv

Output
After running the script, you will find a new CSV file named modified_data.csv in the same directory. This file contains the cleaned and processed data.

Example

Average Age: 35.2
Median Salary (EGP): 95000.0
Ratio of Males to Females: 1.25


