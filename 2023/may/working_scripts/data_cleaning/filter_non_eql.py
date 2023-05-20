import pandas as pd

file1 = 'file1.csv'
file2 = 'file2.csv'
file3 = './filterd_prod_may02up.xlsx'
colums = ['Internal Reference','Products/Attribute Values/Value','Products/ID','Product/Product Template/ID']
# Read data from file1
df1 = pd.read_excel('../../Master Files/ToBeUpdated.xlsx', sheet_name='Sheet1')

# Read data from file2
df2 = pd.read_excel('./product_template_removed_duplicates.xlsx', sheet_name='Sheet1')

# Merge dataframes based on columns A and B
merged_df = pd.merge(df1, df2, on=['Internal Reference','Products/Attribute Values/Value'], how='inner')
print(merged_df.head(5))

# Select columns A, B, C, and D from the merged dataframe
# match_rows = merged_df[['Internal Reference','Products/Attribute Values/Value','Products/ID','Product/Product Template/ID']]

# Rename columns
# match_rows.columns = ['Internal Reference','Products/Attribute Values/Value','Products/ID','Product/Product Template/ID']

# Save match_rows to file3
merged_df.to_excel(file3, index=False)
