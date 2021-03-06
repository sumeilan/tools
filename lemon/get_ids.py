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
    type11 = []
    type12 = []
    type51 = []
    for i in datas:
        if get_type(i,'9') is not None:
            type9.append(int(get_type(i,'9')[0]))

        if get_type(i,'10') is not None:
            type10.append(int(get_type(i,'10')[0]))

        if get_type(i,'11') is not None:
            type11.append(int(get_type(i,'11')[0]))

        if get_type(i,'12') is not None:
            type12.append(int(get_type(i,'12')[0]))

        if get_type(i,'51') is not None:
            type51.append(int(get_type(i,'51')[0]))



    print('type=9',type9)
    print('type=10', type10)
    # print('type=11', type11)
    # print('type=12', type12)
    # print('type=51', type51)

url = 'http://api-demo.lemondream.cn/api/recommend/get_recommend_content_list'
device_token = random.sample(range(1,20), 1)  # 生成2个随机数，范围是1-100
for i in device_token:
    params = {'page':'1', 'pageSize': '20', 'app_key': 'lemondream','scene_id':'2001','device_token':i}
    Authorization = HmacSHA256.sh258(json.dumps(params))
    AuthorizationV2 = HmacSHA256.sh258_v2(json.dumps(params))
    bidata = '{"appDeviceId":"' + str(i) + '"}'
    header = {
        "Content-Type": "application/json",
        "channel": "default",
        "X-Token": "4b5e4c5a02",
        "versionCode": "android_2.1.0",
        "Authorization": Authorization,
        "AuthorizationV2": AuthorizationV2,
        "biData": str(bidata)
    }
    response = requests.post(url, json=params, headers=header, verify=False)
    # print(response)
    datas = response.json()['data']['list']
    total(datas)



