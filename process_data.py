import more_sheets
import re
import pandas


#excel数据去除多余的空行、重复的数据
def clear_blank_line():
    new1 = []
    new2 = []

    data_source = 'E:\\python\\tools\\datas\\test.xlsx'
    output_data = 'E:\\python\\tools\\datas\\test493.xlsx'
    exceldatas = more_sheets.excel_to_json(data_source)
    for i in range(len(exceldatas)):
        for y in range(len(exceldatas[i])):
            # new = re.sub(r'[\n]+', r'\n', exceldatas[i][y], flags=re.S)#去除多余空格
            new = re.sub(r'[ ]+', r'\n', exceldatas[i][y], flags=re.S)#空格替换为换行符
            new1.append(new)
        new2.append(new1)
        new1 = []

    more_sheets.json_to_excel_new(new2,output_data)
    data = pandas.DataFrame(pandas.read_excel(output_data))
    no_re_row = data.drop_duplicates()  #删除重复的行
    no_re_row.to_excel(output_data)
    for indexs in data.index:
        for i in range(len(data.loc[indexs].values)):
            if '？？' in str(data.loc[indexs].values[i]):
                print(indexs,i)
                more_sheets.fill_cell('E:\\python\\tools\\datas\\test493.xlsx',[[indexs+1,i+1]])
            if '??' in str(data.loc[indexs].values[i]):
                print(indexs, i)
                more_sheets.fill_cell(output_data,[[indexs+1,i+1]])



if __name__ == '__main__':
	clear_blank_line()

