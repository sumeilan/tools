#homepagezonelist
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

def get_zone_id(datas):
    zoneid = r'\'zone_id\': [(\-|\+)?\d]+'  # 模式字符串
    zone_id = re.findall(zoneid, str(datas), re.I)  # 匹配字符串不区分大小
    title_pattern = '\'title\': \'[a-zA-Z0-9\u4E00-\u9FA5\uf900-\ufa2d]+\''
    title_num = re.findall(title_pattern, str(datas), re.I)

    if zone_id:
        return dict(zip(zone_id,title_num))
    else:
        return None

url= 'http://api-api2.lemondream.cn/api/recommend/get_home_page_zone_list'
# url= 'http://lemondream.chumanapp.com/api/recommend/get_home_page_zone_list'

device_token = random.sample(range(1,100),10)  # 生成2个随机数，范围是1-100
act_total = []
for i in device_token:
    params = {'page':'1', 'pageSize': '20', 'app_key': 'lemondream','scene_id':'2001','device_token':i}
    Authorization = HmacSHA256.sh258(json.dumps(params))
    bidata = '{"appDeviceId":"'+ str(i) +'"}'
    header = {
        "Content-Type": "application/json",
        "channel": "default",
        "X-Token": "4b5e4c5a02",
        "Authorization": Authorization,
        "biData":str(bidata)
    }
    response = requests.post(url, json=params, headers=header, verify=False)
    datas = response.json()['data']
    act_id = get_act_id(datas)
    zone_id = get_zone_id(datas)
    print(act_id)
    print(zone_id)


