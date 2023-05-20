# dropna() method is used to remove the rows with missing values and drop_duplicates() method is used to remove the duplicate rows. The keep parameter is used to specify the first or last occurrence of the duplicate values. The default value of keep parameter is first. The inplace parameter is used to specify whether to make the changes in the original DataFrame or not. The default value of inplace parameter is False.
import pandas
import numpy as np

colums = ['Reference','Pricegroup','Product','Template']
excel_data_df = pandas.read_excel('../../Master Files/ToBeUpdated.xlsx', sheet_name='Sheet1')
excel_data_df2 = pandas.read_excel('../../Master Files/May Product Template new.xlsx', sheet_name='template')
excel_data_df['Template'] = np.where(((excel_data_df['Reference'] == excel_data_df2['Reference']) & (excel_data_df['Pricegroup'] == excel_data_df2['Pricegroup'] ) ), excel_data_df2['Template'], '')
excel_data_df['Product'] = np.where( ( (excel_data_df['Reference'] == excel_data_df2['Reference']) & (excel_data_df['Pricegroup'] == excel_data_df2['Pricegroup'] ) ), excel_data_df2['Product'], '')

excel_data_df.to_excel('./filterd_prod_may02.xlsx', sheet_name='template',index=True,header=colums)
