# remove duplicates from excel file
import pandas
import numpy as np

colums = [
    'Internal Reference',
    'Pricelist Rules/Product Variant/ID',
    'Pricelist Rules/Product/ID',
    'Products/Product Template',
    'Products/Attribute Values',
    'Products/Attribute Values/Value',
    'Pricelist Rules/Apply On',
    'Pricelist Rules',
    'EUR rec.',
    'DKK rec.',
    'NOK rec.',
    'SEK rec.',
    'EUR ExW',
    'EUR DAP',
    'SEK KK-A',
    'SEK KK-B'
    ]
excel_data_df = pandas.read_excel('../Master File/Masterfile_230504_11.xlsx', sheet_name='Exp-P1d', usecols=colums)
excel_data_df['Pricelist Rules/Product/ID'].replace('', np.nan, inplace=True)
excel_data_df.dropna(subset=['Pricelist Rules/Product/ID'], inplace=True)
excel_data_df.drop_duplicates(subset=['Internal Reference', 'Products/Attribute Values/Value'], keep='first', inplace=True)
excel_data_df.drop_duplicates(subset=['Internal Reference', 'Pricelist Rules/Product/ID'], keep='first', inplace=True)
excel_data_df.to_excel('../generated_pricelists/Cleaned Masterfile_230504.xlsx',index=True,header=colums)