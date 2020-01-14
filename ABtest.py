import requests
import re, random, numpy,HmacSHA256,json

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
    print('-------备注：10=爬虫视频，9=爬虫图片，4=漫画，2=漫剧-------')
    print('总数=',len(type),' 各个类型及对应数量', dict(zip(numpy.unique(num), tdata)))

    if type:
        return type
    else:
        return None

url = 'http://api.lemondream.cn/api/recommend/get_recommend_content_list'

device_token = random.sample(range(1,20), 10)  # 生成2个随机数，范围是1-100
act_total = []
for i in device_token:
    params = {'page':'1', 'pageSize': '20', 'app_key': 'lemondream','scene_id':'2001','device_token':i}
    Authorization = HmacSHA256.sh258(json.dumps(params))
    header = {
        "Content-Type": "application/json",
        "channel": "default",
        "X-Token": "4b5e4c5a02",
        "Authorization": Authorization
    }
    response = requests.post(url, json=params, headers=header, verify=False)
    act_id = get_act_id(response.json()['data'])
    act_total.append(act_id[0])
    show_tag_type = get_show_tag_type(response.json()['data'])
    print('\n', 'device_token=', i)
    print(act_id, show_tag_type)
    print(response.text)
    get_type(response.json()['data'])

tt = []
for i in numpy.unique(act_total):
    tt.append(sorted(act_total).count(i))
print('\n', dict(zip(numpy.unique(act_total), tt)))
