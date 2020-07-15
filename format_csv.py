import pandas as pd
import csv, os, sys


# 删除所有行
def del_all_row(file):
    datas = pd.read_csv(file)
    data = datas.drop(range(len(datas)))  # 删除前10行
    data.to_csv(file, index=0)


# 删除前N行
def del_some_row(file, num):
    data = pd.read_csv(file)
    data = data.drop(range(num))  # 删除前10行
    data.to_csv(file, index=0)


# 删除某列
def del_some_col(file, num):
    data = pd.read_csv(file)
    cols = data.columns  # 所有列
    data = data.drop([cols[num]], axis=1)  # 删除这列数据
    data.to_csv(file, index=0)


# 删除全部列
def del_all_col(file):
    data = pd.read_csv(file)
    cols = data.columns
    for col in cols:
        data = data.drop([col], axis=1)  # 删除这列数据
    data.to_csv(file, index=0)

def options(param,file,*num):
    # print(param,file,num[0])
    if param == 'del_all_row':
        del_all_row(file)
    elif param == 'del_some_row':
        del_some_row(file,int(num[0]))
    elif param == 'del_all_col':
        del_all_col(file)
    else:
        del_some_col(file,int(num[0]))


if __name__ == '__main__':
    if len(sys.argv) > 3:
        file_name = sys.argv[1]
        param = sys.argv[2]
        num = sys.argv[3]
        options(param,file_name,num)

    elif len(sys.argv) > 2:
        file_name = sys.argv[1]
        param = sys.argv[2]
        options(param, file_name)

    else:
        print('缺少参数')








        



