# extract2.py is a Python script that extracts data from two Excel files and merges them into a new Excel file.
import pandas as pd

# Read the first Excel file
file1_df = pd.read_excel('../Master File/masterfile_230307.xlsx',sheet_name='products_template')

# Read the second Excel file
file2_df =  pd.read_excel('../Master File/masterfile_230307.xlsx',sheet_name='Sheet2')

# Merge the DataFrames on Lock ID and Product/Attribute Values/Value
merged_df = pd.merge(file1_df, file2_df, on=['Lock IDs', 'Products/Attribute Values/Value'])

# Extract the desired columns from the merged DataFrame
colums = ['Lock IDs', 'Products/Attribute Values/Value','Products/ID','Product Template ID','Pricelist Rules/Apply On','EUR_item_ids/fixed_price',	'DKK_item_ids/fixed_price',	'NOK_item_ids/fixed_price',	'SEK_item_ids/fixed_price']

result_df = merged_df[colums]

# Save the result to a new Excel file
result_df.to_excel('../Master File/result_may.xlsx', index=False)