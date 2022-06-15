# pandas_sheet_name

import pandas as pd
import numpy as np
# pip install openpyxl
# pip install xlrd

# открыть xls таблицу на чтение
with pd.ExcelFile('WeightLoss.xls') as r:
    sheet1 = pd.read_excel(r, sheet_name=1) # 'Sheet1'
    print(sheet1, end='\n\n')
    sheet2 = pd.read_excel(r, sheet_name=2) # 'Sheet2'
    print(sheet2, end='\n\n')

# Обычное сохранение только одного листа xlsx
# sheet2.to_excel('New_file.xlsx', sheet_name='x1')
# sheet2.to_excel('New_file.xlsx', index_label='index', sheet_name='x1')

# Особое сохранение нескольких листов xlsx
# pip install xlsxwriter
# writer = pd.ExcelWriter('name.xlsx', engine='xlsxwriter')
# df1.to_excel(writer, sheet_name='x1')
# df2.to_excel(writer, sheet_name='x2')
# df2.to_excel(writer, sheet_name='x3')
# writer.save() # метод .save() используется для сохранения данных
# # writer.close() # метод .close() используется при открытии файла в ходе выполнения программы несколько раз

# Ещё один пример использования 'xlsxwriter'

# Create a Pandas dataframe from the data.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
# print(df)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

with pd.ExcelFile('pandas_simple.xlsx') as r:
    sheet1 = pd.read_excel(r, sheet_name=0) # 'Sheet1'
    print(sheet1)
