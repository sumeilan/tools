# -*- coding: utf-8 -*-
import os, sys, json


# 判断文件后缀
def file_type(path):
    file = os.path.splitext(path)
    filename, type = file
    # print(filename,type)
    return type


# 获取当前路径下的所有子目录
def files(file_dir):
    fs = []
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        for file in files:
            if file_type(file) == '.html':
                fs.append(file)
        return fs


def file_data(file_name):
    # data = '{"code":0,"msg":"","count":10,"data":[{"id":10,"file":"2020-07-27.html","option":"查看"},{"id":10,"file":"2020-07-27.html","option":"查看"}]}'
    fs = files(file_name)
    data = []
    i = 0
    for f in fs:
        i = i+1
        data.append({"id": i, "file": f})
    count = 10
    file_datas = {"code": "0", "msg": "操作成功", "count": count, "data": data}
    return json.dumps(file_datas)


if __name__ == '__main__':
    # file_name = 'E:\\python\\testcase\\report'
    # data = file_data(file_name)
    # print(data)
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        data = file_data(file_name)
        print(data)
