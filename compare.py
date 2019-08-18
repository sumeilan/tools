import excel_to_json
import json

json_file = 'E:\\test_python\\tools\\all_json.json'
excel_file = 'E:\\test_python\\tools\\test1.xlsx'
excel_datas = excel_to_json.excel_to_json(excel_file)
with open(json_file, 'r') as f:
	json_datas = json.load(f)
is_pass = []

for y in range(len(excel_datas)):
    for i in range(len(json_datas)):
        if y not in is_pass:
            if 'refer' in json_datas[i]['ext']:
	            if json_datas[i]['ext']['refer'] == excel_datas[y][5]:
		            if json_datas[i]['ext']['pos'] == excel_datas[y][4]:
			            if str(
					            json_datas[i]['ext']['tag']) == str(
				            excel_datas[y][2]) and json_datas[i]['ext']['act'] == excel_datas[y][3] and str(
				            json_datas[i]['event_id']) == str(
				            excel_datas[y][6]):

				            if len(json_datas[i]['ext']['value']) == 0 and excel_datas[y][7] == '':
					            print('第' + str(y+1) + '条测试通过')
					            is_pass.append(y)
					            excel_to_json.fill_cell(excel_file, [[y, 0]])
					            break

				            elif len(json_datas[i]['ext']['value']) > 0 and excel_datas[y][7] is not None:
					            print('第' + str(y+1) + '条测试通过')
					            is_pass.append(y)
					            excel_to_json.fill_cell(excel_file, [[y, 0]])
					            break
				            else:
					            print(
						            '第' + str(y+1) + '条测试不通过:value不一致-----------', '实际value：:',
						            json_datas[i]['ext']['value'], '期望value:',
						            excel_datas[y][7])

			            else:
				            print(
					            '第' + str(y+1) + '条测试不通过-----------',
					            '期望tag:', excel_datas[y][2],
					            '实际tag:', json_datas[i]['ext']['tag'],
					            '期望act:', excel_datas[y][3],
					            '实际act:', json_datas[i]['ext']['act'],
					            '期望tag:', excel_datas[y][4],
					            '实际tag:', json_datas[i]['ext']['pos'],
					            '期望tag:', excel_datas[y][5],
					            '实际tag:', json_datas[i]['ext']['refer'],
					            '期望event_id:', excel_datas[y][6],
					            '实际event_id:', json_datas[i]['event_id'])
		            else:
			            print(json_datas[i]['ext'])
			            print('第' + str(y+1) + '条测试不通过-----------', '实际pos:', json_datas[i]['ext']['pos'], '期望refer:',
			                  excel_datas[y][4])

