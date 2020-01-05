import json
import re

# 将txt数据转为json
datas = []
jdata = []


def txt_to_json(f_path):
    with open(f_path) as f:
        for line in f:
            line = line.strip('\n')
            line = line.strip('\[').strip('\]')
            if len(line) > 0:
                # print('line',line,type(line))
                line1 = line.replace("},{", "}|{")
                datas.append(line1.split('|'))

        for da in datas:
            for d in da:
                jdata.append(json.loads(d))
        # print(jdata)
        return jdata


if __name__ == '__main__':
    f_path = 'E:\\test_python\\tools\\datas\\testdatas.txt'
    txt_to_json(f_path)
