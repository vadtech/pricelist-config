import pandas
colums = ['NOK_Pricelist_ID','NOK_Pricelist Name','NOK_Currency','Product Template ID','Products/ID','Pricelist Rules/Apply On','NOK_item_ids/fixed_price']
excel_data_df = pandas.read_excel('../Master File/masterfile_230307.xlsx', sheet_name='base_list', usecols=colums)


excel_data_df.loc[excel_data_df['Pricelist Rules/Apply On'] == 'Product', 'Products/ID'] = 'FALSE'

excel_data_df.loc[excel_data_df['Pricelist Rules/Apply On'] == 'Product Variant', 'Product Template ID'] = 'FALSE'

# excel_data_df = excel_data_df.drop("Variants", axis=1, inplace=True)
# excel_data_df = excel_data_df.reset_index(drop=True)
pricelist_column_names=['id','name','currency_id','item_ids/product_tmpl_id/id','item_ids/product_id/id','item_ids/applied_on','item_ids','item_ids/fixed_price']
excel_data_df.to_excel('../generated_pricelists/NOK_pricelist_230307.xlsx',index=True,header=pricelist_column_names)