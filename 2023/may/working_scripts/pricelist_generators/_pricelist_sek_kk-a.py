import pandas
colums = ['SEK KK-A_Pricelist_ID','SEK KK-A_Pricelist Name','SEK KK-A_Currency','Pricelist Rules/Product Variant/ID','Pricelist Rules/Product/ID','Pricelist Rules/Apply On','SEK KK-A']
excel_data_df = pandas.read_excel('../../master_files/Pricelist Masterfile_230520.xlsx', sheet_name='baselist', usecols=colums)


excel_data_df.loc[excel_data_df['Pricelist Rules/Apply On'] == 'Product', 'Pricelist Rules/Product/ID'] = 'FALSE'

excel_data_df.loc[excel_data_df['Pricelist Rules/Apply On'] == 'Product Variant', 'Pricelist Rules/Product Variant/ID'] = 'FALSE'

# excel_data_df = excel_data_df.drop("Variants", axis=1, inplace=True)
# excel_data_df = excel_data_df.reset_index(drop=True)
pricelist_column_names=['ID','Pricelist Name','Currency','Pricelist Rules/Product Variant/ID','Pricelist Rules/Product/ID','Pricelist Rules/Apply On','Pricelist Rules/Fixed Price']
excel_data_df.to_excel('../../generated_pricelist/20/SEK KK-A_pricelist_May.xlsx',index=True,header=pricelist_column_names)