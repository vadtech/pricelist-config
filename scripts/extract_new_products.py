import pandas as pd
colums = ['Item No.', 'id','categ_id/id','attribute_line_ids/attribute_id/id','attribute_line_ids/value_ids/id','attribute_line_ids_values','Norwegian Description','English Description','Category']

# Read the first Excel file
masterfile_230307 = pd.read_excel('../Master File/masterfile_230307.xlsx',sheet_name='Exp-P1d', usecols=colums)

# Read the second Excel file
masterfile = pd.read_excel('../Master File/master file.xlsx',sheet_name='Exp-P1d', usecols=colums)

# Extract the internal references from masterfile
internal_refs = set(masterfile['Item No.'])

# Filter the items from masterfile_230307 that are not in internal_refs
filtered_items = masterfile_230307[~masterfile_230307['Item No.'].isin(internal_refs)]

# Extract the columns of the filtered items
filtered_columns = filtered_items[['Item No.', 'id','categ_id/id','attribute_line_ids/attribute_id/id','attribute_line_ids/value_ids/id','attribute_line_ids_values','Norwegian Description','English Description','Category']]

# Save the filtered columns to a new Excel file
filtered_columns.to_excel('../Master File/filtered_items.xlsx', index=False)