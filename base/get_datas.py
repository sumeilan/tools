import json
import re

datas = []
jdata = []


# 根据规则从txt提取数据
def find_phonenum(f_path):
    with open(f_path) as f:
        lines = f.readlines()
        for line in lines:
            regex = re.compile(r'([1][1-9]\d{9})')
            result = regex.findall(line)
            if result:
                print(result)


if __name__ == '__main__':
    f_path = 'E:\\test_python\\tools\\datas\\testdatas.txt'
    find_phonenum(f_path)
