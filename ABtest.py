import requests
import re, random,numpy

def get_act_id(datas):
	actid_pattern = r'\'act_id\': \d+'  # 模式字符串
	act_id = re.findall(actid_pattern, str(datas), re.I)  # 匹配字符串不区分大小
	num_pattern = r'\d+'
	act_num = re.findall(num_pattern, str(act_id), re.I)
	if act_num:
		return act_num
	else:
		return None

def get_show_tag_type(datas):
	showtag_pattern = r'\'show_tag_type\': \d+'  # 模式字符串
	show_tag_type = re.findall(showtag_pattern, str(datas), re.I)  # 匹配字符串不区分大小
	if show_tag_type:
		return show_tag_type
	else:
		return None

def get_type(datas):
	type_pattern = r'\'type\': \'\d+\''  # 模式字符串
	type = re.findall(type_pattern, str(datas), re.I)  # 匹配字符串不区分大小
	num_pattern = r'\'\d+\''
	num = re.findall(num_pattern, str(type), re.I)
	tdata = []
	for i in numpy.unique(num):
		tdata.append(sorted(num).count(i))
	print('总数=', len(type))
	print('各个类型及数量',dict(zip(numpy.unique(num),tdata)))

	if type:
		return type
	else:
		return None

url = 'http://lemondream.chumanapp.com/api/recommend/get_recommend_content_list'
header = {
	'versionCode': 'android_1.2.0',
	'channel': 'default',
	'X-Token': '48584a500142',
	'Authorization': ':82ec573c9e35dghh39e46075hd113j3h',
	'Content-Type': 'application/json; charset=utf-8',
	'Content-Length': 145,
	'Host': 'lemondream.chumanapp.com',
	'Connection': 'Keep-Alive',
	'Accept-Encoding': 'gzip',
	'User-Agent': 'okhttp/3.12.5'
}
device_token = random.sample(range(1, 5), 3)  # 生成2个随机数，范围是1-100
act_total = []
for i in device_token:
	params = {
		"page": "1",
		"pagesize": "20",
		"app_key": "lemondream",
		"scene_id": "2001",
		"device_token": i,
		"access_token": ""
	}
	response = requests.request('post', url, params=params)
	act_id = get_act_id(response.json()['data'])
	act_total.append(act_id[0])
	show_tag_type = get_show_tag_type(response.json()['data'])
	print('\n', 'device_token=', i)
	print(act_id,show_tag_type)
	get_type(response.json()['data'])

tt = []
for i in numpy.unique(act_total):
	tt.append(sorted(act_total).count(i))
print('\n',dict(zip(numpy.unique(act_total),tt)))






