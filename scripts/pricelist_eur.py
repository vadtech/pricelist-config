import pandas
colums = ['EUR_Pricelist_ID','EUR_Pricelist Name','EUR_Currency','Product Template ID','Products/ID','Pricelist Rules/Apply On','EUR_item_ids/fixed_price']
excel_data_df = pandas.read_excel('../Master File/masterfile_230307.xlsx', sheet_name='base_list', usecols=colums)


excel_data_df.loc[excel_data_df['Pricelist Rules/Apply On'] == 'Product', 'Products/ID'] = 'FALSE'

excel_data_df.loc[excel_data_df['Pricelist Rules/Apply On'] == 'Product Variant', 'Product Template ID'] = 'FALSE'

# excel_data_df = excel_data_df.drop("Variants", axis=1, inplace=True)
# excel_data_df = excel_data_df.reset_index(drop=True)
pricelist_column_names=['ID','Pricelist Name','Currency','Pricelist Rules/Product Variant/ID','Pricelist Rules/Product/ID','Pricelist Rules/Apply On','Pricelist Rules/Fixed Price']
excel_data_df.to_excel('../generated_pricelists/EUR_pricelist_230307.xlsx',index=True,header=pricelist_column_names)