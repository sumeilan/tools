import excel_to_json
import re
import numpy,pandas

#excel数据去除多余的空行、重复的数据
def clear_blank_line(output_path,exceldatas,sheet):
    new1 = []
    new2 = []

    for i in range(len(exceldatas)):
        for y in range(len(exceldatas[i])):
            new = re.sub(r'[ ]+', r'\n', exceldatas[i][y], flags=re.S)#空格替换为换行符
            new1.append(new)
        new2.append(new1)
        new1 = []

    excel_to_json.json_to_excel_append(new2,output_path,sheet)
    data = pandas.DataFrame(pandas.read_excel(output_path))
    no_re_row = data.drop_duplicates()  #删除重复的行
    no_re_row.to_excel(output_path,index=False)
    for indexs in data.index:
        for i in range(len(data.loc[indexs].values)):
            if '？？' in str(data.loc[indexs].values[i]):
                excel_to_json.fill_cell(output_path, [[indexs + 1, i]])
            if '??' in str(data.loc[indexs].values[i]):
                excel_to_json.fill_cell(output_path,[[indexs+1,i]])



