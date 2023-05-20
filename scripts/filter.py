# dropna() method is used to remove the rows with missing values and drop_duplicates() method is used to remove the duplicate rows. The keep parameter is used to specify the first or last occurrence of the duplicate values. The default value of keep parameter is first. The inplace parameter is used to specify whether to make the changes in the original DataFrame or not. The default value of inplace parameter is False.
import pandas
import numpy as np

colums = ['Internal Reference','Products/Attribute Values/Value','Products/ID','Pricelist Rules/Product Variant/ID']
excel_data_df = pandas.read_excel('../Master File/Masterfile_230504.xlsx', sheet_name='Exp-P1d')
excel_data_df2 = pandas.read_excel('../Master File/May Product Template new.xlsx', sheet_name='template')
# excel_data_df['Products/Attribute Values/Value'].replace('', np.nan, inplace=True)
# excel_data_df.dropna(subset=['Products/Attribute Values/Value'], inplace=True)
# excel_data_df.drop_duplicates(subset=['Internal Reference', 'Products/Attribute Values/Value'], keep='first', inplace=True)
excel_data_df['Pricelist Rules/Product Variant/ID'] = np.where( ( (excel_data_df['Internal Reference'] == excel_data_df2['Internal Reference']) & (excel_data_df['Products/Attribute Values/Value'] == excel_data_df2['Products/Attribute Values/Value'] ) ), excel_data_df2['Pricelist Rules/Product Variant/ID'], '')
excel_data_df['Products/ID'] = np.where( ( (excel_data_df['Internal Reference'] == excel_data_df2['Internal Reference']) & (excel_data_df['Products/Attribute Values/Value'] == excel_data_df2['Products/Attribute Values/Value'] ) ), excel_data_df2['Products/ID'], '')

excel_data_df.to_excel('../generated pricelists/filterd_prod_may.xlsx', sheet_name='template',index=True,header=colums)