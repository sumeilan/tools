import requests
import re, random, numpy,HmacSHA256,json

#http://api-api2.lemondream.cn/
url= 'http://api-api2.lemondream.cn/api/recommend/get_rec_abtest'
device_token = random.sample(range(30,50),1)  # 生成2个随机数，范围是1-100
act_total = []
for i in device_token:
    params = {'page':'1', 'pageSize': '20', 'app_key': 'lemondream','scene_id':'2001','device_token':i}
    Authorization = HmacSHA256.sh258(json.dumps(params))
    AuthorizationV2 = HmacSHA256.sh258_v2(json.dumps(params))
    bidata = '{"appDeviceId":"'+ str(i) +'"}'
    header = {
        "Content-Type": "application/json",
        "channel": "default",
        "X-Token": "4b5e4c5a02",
        "versionCode" : "android_2.1.0",
        "Authorization": Authorization,
        "AuthorizationV2": AuthorizationV2,
        "biData": str(bidata)
    }
    response = requests.post(url, json=params, headers=header, verify=False)
    datas = response.json()['data']
    print(datas)


