import pandas as pd

# Read the Excel files into DataFrames
file1 = pd.read_excel('../Master File/masterfile_230307.xlsx', sheet_name='products_template')
file2 = pd.read_excel('../Master File/masterfile_230307.xlsx', sheet_name='base_list')

# Merge the DataFrames on the Lock IDs column
merged = pd.merge(file1, file2, on='ID', how='inner')

# Create a new column in file2 with the Lock IDs from file1 where the category is 'product'
file2.loc[file2['Pricelist Rules/Apply On'] == 'Product', 'Product Template ID'] = merged['Lock IDs_x']

# Fill the remaining empty cells in the Lock IDs column with 'FALSE'
file2['Product Template ID'].fillna('FALSE', inplace=True)

# Save the modified file2 DataFrame back to the Excel file
file2.to_excel('../Master File/masterfile_2.xlsx', sheet_name='base_list', index=False)