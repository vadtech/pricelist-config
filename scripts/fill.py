# fill empty cells with previous value
import pandas as pd

# read Excel file into a pandas DataFrame
df = pd.read_excel('../Master File/May Product Template new.xlsx', sheet_name='template')

# fill empty cells with previous value
# Fill empty cells in the Internal Reference column with the previous non-empty cell value
df['Internal Reference'].fillna(method='ffill', inplace=True)

# save the filled DataFrame back to Excel file
df.to_excel('../Master File/May Product Template new.xlsx', sheet_name='template', index=False)