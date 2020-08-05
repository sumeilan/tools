# -*- coding: utf-8 -*-
import os, sys, json
root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root)
import format.format_excel


def case_module(file):
    sheet_name = format.format_excel.get_sheets(file)
    data = []
    i = 0
    for s in sheet_name:
        i = i + 1
        data.append({"id": i, "name": s[0:-1]})
    count = 10
    file_datas = {"code": "0", "msg": "操作成功", "count": count, "data": data}
    return json.dumps(file_datas)


if __name__ == '__main__':
    # file_name = "E:\\python\\tools\\datas\\test2.xlsx"
    # case_module(file_name)
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        data = case_module(file_name)
        print(data)
