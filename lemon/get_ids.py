import re,numpy,random,HmacSHA256,requests,json

def get_obj_id(datas):
    obj_pattern = r'\'obj_id\': \'\d+\''  # 模式字符串
    obj = re.findall(obj_pattern, str(datas), re.I)  # 匹配字符串不区分大小
    id_pattern = r'\d+'  # 模式字符串
    id = re.findall(id_pattern, str(obj), re.I)  # 匹配字符串不区分大小
    if len(id) > 0:
        # print(id[0])
        return id

def get_type(datas,ty):
    type_pattern = r'\'type\': \'\d+\''  # 模式字符串
    type = re.findall(type_pattern, str(datas), re.I)  # 匹配字符串不区分大小
    if type[0].find(ty)>0:
        ids = get_obj_id(datas)
        return ids

def total(datas):
    type9 = []
    type10 = []

    for i in datas:
        # print(i)
        if get_type(i,'9') is not None:
            type9.append(int(get_type(i,'9')[0]))

        if get_type(i,'10') is not None:
            type10.append(int(get_type(i,'10')[0]))

    print('type=9',type9)
    print('type=10', type10)

url = 'http://api-demo.lemondream.cn/api/recommend/get_recommend_content_list'
device_token = random.sample(range(1,20), 1)  # 生成2个随机数，范围是1-100
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
    datas = response.json()['data']['list']
    total(datas)



