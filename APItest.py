import requests
import random,json
import HmacSHA256

def url():
    url = 'http://api.lemondream.cn/api/recommend/get_recommend_content_list'
    device_token = random.sample(range(1, 2), 1)  # 生成2个随机数，范围是1-100
    for i in device_token:
        params = {'page': '1', 'pageSize': '20', 'app_key': 'lemondream', 'scene_id': '2001', 'device_token': i}
        Authorization = HmacSHA256.sh258(json.dumps(params))
        header = {
            "Content-Type": "application/json",
            "channel": "default",
            "X-Token": "4b5e4c5a02",
            "Authorization": Authorization
        }
        response = requests.post(url, json=params, headers=header, verify=False)
        datas = response.json()['data']
        return datas
datas = url()
print(datas)







