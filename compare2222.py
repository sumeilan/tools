import excel_to_json
import txt_to_json
import merge_json

json_file = 'E:\\test_python\\tools\\datas\\all_json.json'
excel_file = 'E:\\test_python\\tools\\datas\\test1.xlsx'
txt_path = 'E:\\test_python\\tools\\datas\\request1.txt'
excel_datas = excel_to_json.excel_to_json(excel_file)
report_file = r'E:\\test_python\\tools\\datas\\test.txt'
#txt 文件存储json数据
json_datas = txt_to_json.txt_to_json(txt_path)
# print('json_dd',json_datas)
# 合并多个json文件
merge_json.read_json()
# with open(json_file, 'r') as f:
#     json_datas = json.load(f)
#     print('json_datas',json_datas)

is_pass = []
fail_result = ''
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
                            if len(
                                    json_datas[i]['ext']['value']) == 0 and excel_datas[y][7] == '':
                                pass_result =  '实际value：:', json_datas[i]['ext']['value'], '期望value:', excel_datas[y][7]
                                print('第' + str(y + 1) + '条测试通过')
                                print(pass_result)
                                is_pass.append(y)
                                excel_to_json.fill_cell(excel_file, [[y, 0]])
                                break

                            elif len(json_datas[i]['ext']['value']) > 0 and excel_datas[y][7] is not None:
                                value = list(filter(None, json_datas[i]['ext']['value']))
                                if len(value ) >0:
                                    pass_result = '实际value：:', json_datas[i]['ext']['value'], '期望value:', \
                                                  excel_datas[y][7]
                                    print('第' + str(y + 1) + '条测试通过')

                                    print(pass_result)
                                    is_pass.append(y)
                                    excel_to_json.fill_pass_cell(
                                        excel_file, [[y, 0]])
                                    break

                            else:
                                print('bbbbbbbbbbb')
                                fail_result = "value不一致--" + "实际value为:" + " ".join(json_datas[i]['ext']['value'])
                                print(fail_result)
                                excel_to_json.fill_fail_cell(excel_file, [[y, 8]], fail_result)
                                print(
                                    '第' + str(y + 1) + '条测试不通过:value不一致-----------', '实际value：:',
                                    json_datas[i]['ext']['value'], '期望value:',
                                    excel_datas[y][7])

                        else:
                            fail_result = "tag-"+str(json_datas[i]['ext']['tag'])+" ext-"+json_datas[i]['ext']['act']+" pos-"\
	                                 +json_datas[i]['ext']['pos']+" refer-"+json_datas[i]['ext']['refer']\
	                                 +" eventd-"+json_datas[i]['event_id']+" valueI-"+" ".join(json_datas[i]['ext']['value'])
                            excel_to_json.fill_fail_cell(
                            excel_file, [[y, 8]], fail_result)
                            print(
                                'aa第' + str(y + 1) + '条测试不通过-----------',
                                '期望tag:', excel_datas[y][2],
                                '实际tag:', json_datas[i]['ext']['tag'],
                                '期望act:', excel_datas[y][3],
                                '实际act:', json_datas[i]['ext']['act'],
                                '期望pos:', excel_datas[y][4],
                                '实际pos:', json_datas[i]['ext']['pos'],
                                '期望refer:', excel_datas[y][5],
                                '实际refer:', json_datas[i]['ext']['refer'],
                                '期望event_id:', excel_datas[y][6],
                                '实际event_id:', json_datas[i]['event_id'])
                    else:
                        print(json_datas[i]['ext'])
                        fail_result = '第' + str(y + 1) + '条测试不通过:value不一致-----------', '实际value：:', json_datas[i]['ext'][
                            'value'], '期望value:', excel_datas[y][7]
                        excel_to_json.fill_fail_cell(
                            excel_file, [[y, 8]], fail_result)
                        print('第' + str(y + 1) + '条测试不通过-----------',
                              '实际pos:',
                              json_datas[i]['ext']['pos'],
                              '期望refer:',
                              excel_datas[y][4])
