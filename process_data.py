import more_sheets
import re,numpy
import pandas
import pytz,dateutil,xlrd


#excel数据去除多余的空行
def clear_blank_line():
	new1 = []
	new2 = []

	exceldatas = more_sheets.excel_to_json('E:\\test_python\\tools\\datas\\493.xlsx')
	for i in range(len(exceldatas)):

		for y in range(len(exceldatas[i])):
			# new = re.sub(r'[\n]+', r'\n', exceldatas[i][y], flags=re.S)#去除多余空格
			new = re.sub(r'[ ]+', r'\n', exceldatas[i][y], flags=re.S)#空格替换为换行符
			new1.append(new)
		new2.append(new1)
		new1 = []

	more_sheets.json_to_excel_new(new2,'test493.xlsx')
	data = pandas.DataFrame(pandas.read_excel('test493.xlsx'))
	no_re_row = data.drop_duplicates()  #删除重复的行
	no_re_row.to_excel("test493.xlsx")



if __name__ == '__main__':
	clear_blank_line()
