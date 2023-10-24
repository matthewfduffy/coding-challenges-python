"""
Reads an Excel file using openpyxl engine and stores the data in a pandas DataFrame called df

"""

# pip install openpyxl
import pandas as pd

df = pd.read_excel("nameOfExcelFile.xlsx", engine="openpyxl")