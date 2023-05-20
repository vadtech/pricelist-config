import pandas as pd

# Load the Excel file into a pandas dataframe
df_exp_p1d = pd.read_excel('../Master File/Masterfile_230504.xlsx', sheet_name='Exp-P1d')
df_template = pd.read_excel('../Master File/Masterfile_230504.xlsx', sheet_name='template')
colums = ['Internal Reference','Products/Attribute Values/Value','Products/ID','Pricelist Rules/Product Variant/ID']
# Merge the two dataframes based on columns A and B
merged_df = pd.merge(df_exp_p1d, df_template, on=['Internal Reference','Products/Attribute Values/Value'], how='left')

print('merged_df')
print(merged_df.head())
# Populate columns C, D, and E in Exp-P1d sheet with the corresponding values from template sheet
# df_exp_p1d['Products/ID'] = merged_df['C_y']
# df_exp_p1d['Products/Attribute Values/Value'] = merged_df['D_y']
# df_exp_p1d['Products/Product Template'] = merged_df['E_y']

# Save the changes to the Excel file
with pd.ExcelWriter('../Master File/Masterfile_230504_11.xlsx') as writer:
    merged_df.to_excel(writer, sheet_name='Exp-P1d', index=False)
