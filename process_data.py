import excel_to_json
import re,numpy

#excel数据去除多余的空行
def clear_blank_line():
	new1 = []
	new2 = []

	exceldatas = excel_to_json.excel_to_json('E:\\test_python\\tools\\datas\\test3.xlsx')
	print(exceldatas)
	for i in range(len(exceldatas)):

		for y in range(len(exceldatas[i])):
			# new = re.sub(r'[\n]+', r'\n', exceldatas[i][y], flags=re.S)#去除多余空格
			new = re.sub(r' ', r'\n', exceldatas[i][y], flags=re.S)#空格替换为换行符
			new1.append(new)
		new2.append(new1)
		new1 = []
	print(new2)
	excel_to_json.json_to_excel_new(new2,'test4.xlsx')

if __name__ == '__main__':
	clear_blank_line()
