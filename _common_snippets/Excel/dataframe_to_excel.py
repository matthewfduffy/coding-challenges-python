"""
Write a dataframe to Excel (three options)
"""

#  pip install openpyxl

import pandas as pd

# Option #1: Write to a new Excel file with multiple sheets
with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='sheet_name_1')
    df2.to_excel(writer, sheet_name='sheet_name_2')


# Option #2: Write to an existing Excel File
with pd.ExcelWriter('output.xlsx', engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
    df3.to_excel(writer, sheet_name='sheet_name_3')


# Option #3: Simple write to Excel
df.to_excel("output.xlsx")