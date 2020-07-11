import requests
import re, random, numpy,HmacSHA256,json
import total_ABtest
def get_access_token(datas):
    token_pattern = r'\'access_token\': \'[A-Za-z0-9]+\''  # 模式字符串
    access_token = re.findall(token_pattern, str(datas), re.I)  # 匹配字符串不区分大小
    token = access_token[0]
    if token:
        return token[17:-1]
    else:
        return None

url = 'http://lemondream.chumanapp.com/api/recommend/get_rec_abtest'
get_token_url = 'http://api-demo.lemondream.cn/api/sample/token'
device_token = random.sample(range(1,3),2)  # 生成2个随机数，范围是1-100

for i in device_token:
    params = {'device_token':i,'user_id':i}
    Authorization = HmacSHA256.sh258(json.dumps(params))
    header = {
        "Content-Type": "application/json",
        "channel": "default",
        "X-Token": "4b5e4c5a02",
        "Authorization": Authorization
    }
    # response = requests.post(get_token_url, json=params, headers=header, verify=False)
    # datas = response.json()['data']
    # print(response.text)
    # token = get_access_token(datas)
    ab_params = {'scene_id':'2002','device_token':i,'appDeviceId':i}
    ab_Authorization = HmacSHA256.sh258(json.dumps(ab_params))
    ab_header = {
        "Content-Type": "application/json",
        "channel": "default",
        "X-Token": "4b5e4c5a02",
        "Authorization": ':82ec573c9e35dghh39e46075hd113j3h'
    }
    ab_response = requests.post(url, json=ab_params, headers=ab_header, verify=False)
    print(ab_params)
    print(ab_response.text)



