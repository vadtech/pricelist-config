# remove duplicates from excel file
import pandas
import numpy as np

colums = ['Internal Reference',	'Products/Attribute Values/Value',	'Products/ID',	'Product/Product Template/ID']

excel_data_df = pandas.read_excel('./Product Template-check1.xlsx')
excel_data_df.drop_duplicates(subset=['Internal Reference','Products/Attribute Values/Value'], keep='first', inplace=True)
# excel_data_df.drop_duplicates(subset=['Reference', 'Pricelist Rules/Product/ID'], keep='first', inplace=True)
excel_data_df.to_excel('./product_template_removed_duplicates.xlsx',index=True,header=colums)