import pandas as pd
import xlrd
import excel_to_json
import os
import process_data

root = os.getcwd() #获取当前路径
excel_name = root + r'\datas\柠檬精1.0.xlsx'
output_path = root + r'\datas\柠檬精.xlsx'
wb = xlrd.open_workbook(excel_name)
sheets = wb.sheet_names()

for sheet in sheets:
    datas = excel_to_json.excel_to_json(excel_name,sheet)
    print(sheet)
    # output_path = root + r'\datas\柠檬精.xlsx'
    output_path = root + r'\datas\柠檬精' + sheet +'.xlsx'
    process_data.clear_blank_line(output_path,datas,sheet)
