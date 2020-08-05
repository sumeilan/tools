#!/usr/bin/env python
# -*- coding:utf-8 -*-

from xlrd import open_workbook
from xlutils.copy import copy
import os, sys


def save_case(file, sheet_id, case):
    r_xls = open_workbook(file)  # 读取excel文件
    row = r_xls.sheets()[int(sheet_id)].nrows  # 获取已有的行数
    excel = copy(r_xls)  # 将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(int(sheet_id))  # 获取要操作的sheet
    print(case[4])
    if len(case)>0:
        if case[1] =='0':
            module = "首页"

        # 对excel表追加一行内容
        table.write(row, 0, row)  # case_id
        table.write(row, 1, case[0])  # case_name
        table.write(row, 2, module)  # 模块
        table.write(row, 3, case[2])  # url
        table.write(row, 4, case[3])  # request_method
        table.write(row, 5, case[4])  # request_headers
        table.write(row, 6, case[5])  # request_parameter
        # table.write(row, 7, case[6])  # data_from_response
        # table.write(row, 8, case[7])  # request_depend_data
        table.write(row, 9, case[6])  # expect_result
        table.write(row, 11, 'yes')  # is_run
        excel.save(file)  # 保存并覆盖文件


if __name__ == '__main__':
    # file_name = 'E:\\python\\tools\\datas\\test2.xlsx'
    # sheet_id = 0
    # case = ["case_name", "module", "url", "request_method", "request_headers", "request_parameter",
    #         "data_from_response", "request_depend_data", "expect_result"]
    root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    file_name = sys.argv[1]
    sheet_id = int(sys.argv[2])
    case = sys.argv[3].split('@')
    save_case(file_name, sheet_id, case)
