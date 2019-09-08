import excel_to_json
import txt_to_json
import compare

#测试埋点数据
json_file = 'E:\\test_python\\tools\\datas\\all_json.json'
excel_file = 'E:\\test_python\\tools\\datas\\test1.xlsx'
txt_path = 'E:\\test_python\\tools\\datas\\request1.txt'
report_file = r'E:\\test_python\\tools\\datas\\test.txt'

excel_datas = excel_to_json.excel_to_json(excel_file)
json_datas = txt_to_json.txt_to_json(txt_path)  # txt 文件存储json数据
is_pass = []  # 存储通过的记录
refer = False
for y in range(1, len(excel_datas)):
    for i in range(len(json_datas)):
        if y not in is_pass:
            try:
                if 'refer' in json_datas[i]['ext']:
                    refer = compare.compare_refer(
                        json_datas[i]['ext']['refer'], excel_datas[y][5])
                else:
                    if excel_datas[y][5] == '':
                        refer = True

            except Exception as e:
                print('异常啦')
            finally:
                act = compare.compare_act(
                    json_datas[i]['ext']['act'], excel_datas[y][3])
                pos = compare.compare_pos(
                    json_datas[i]['ext']['pos'], excel_datas[y][4])
                tag = compare.compare_tag(
                    json_datas[i]['ext']['tag'], excel_datas[y][2])
                event_id = compare.compare_event_id(
                    json_datas[i]['event_id'], excel_datas[y][6])
                value = compare.compare_value(
                    json_datas[i]['ext']['value'], excel_datas[y][7])
            if refer and act and pos and tag and event_id and value:
                print('第' + str(y + 1) + '条测试通过')
                is_pass.append(y)
                excel_to_json.fill_pass_cell(excel_file, [[y, 0]], [[y, 8]])
                break

            elif act and pos:
                if refer:
                    fail_result = 'value-' + str(json_datas[i]['ext']['value']) + '，refer-' + str(
                        json_datas[i]['ext']['refer']) + ',event_id-' + str(json_datas[i]['event_id'])
                    excel_to_json.fill_fail_cell(
                        excel_file, [[y, 8]], fail_result)
                    print('第' + str(y + 1) + '条测试不通过', 'refer对的')
                    print(fail_result)
                    break
                else:
                    fail_result = 'value-' + str(json_datas[i]['ext']['value']) + '，refer-' + str(
	                    json_datas[i]['ext']['refer']) + ',event_id-' + str(json_datas[i]['event_id'])
                    excel_to_json.fill_fail_cell(excel_file, [[y, 8]], fail_result)
                    print('第' + str(y + 1) + '条测试不通过', )
                    print(fail_result)
