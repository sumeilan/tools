import re,numpy,random,HmacSHA256,requests,json
def get_rec_package_id(datas):
    package_id_pattern = r'\'rec_package_id\': \'[a-z]+\''  # 模式字符串
    rec_package_id = re.findall(package_id_pattern, str(datas), re.I)  # 匹配字符串不区分大小
    pac_pattern = r'\'[a-z]+\''
    pac = re.findall(pac_pattern, str(rec_package_id), re.I)
    if pac:
        return pac
    else:
        return None


def get_type(datas,ty):
    type_pattern = r'\'type\': \'\d+\''  # 模式字符串
    type = re.findall(type_pattern, str(datas), re.I)  # 匹配字符串不区分大小
    if type[0].find(ty)>0:
        print(type[0],ty)
        package_id = get_rec_package_id(datas)
        return package_id

def total(datas):
    type9 = []
    type10 = []
    total9 = []
    total10 = []
    for i in datas:
        print(i)
        if get_type(i,'9') is not None:
            print(get_type(i,'9'))
            type9.append(get_type(i,'9')[0])
        if get_type(i,'10') is not None:
            type10.append(get_type(i,'10')[0])
    for i in numpy.unique(type9):
        total9.append(sorted(type9).count(i))
    print('type=9爬虫内容',dict(zip(numpy.unique(type9), total9)))
    for i in numpy.unique(type10):
        total10.append(sorted(type10).count(i))
    print('type=10爬虫内容', dict(zip(numpy.unique(type10), total10)))

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
    # print(datas)


