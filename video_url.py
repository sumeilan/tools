import requests,re
#http://m-api2.lemondream.cn/m/lemondream/index.html?timestamp=1591778695#/video/MjAwNTEwMTQw?product_type=2

url = input('请输入地址：')
# url = 'http://m-api2.lemondream.cn/m/lemondream/index.html?timestamp=1591778695#/video/MjAwNTEwMTQw?product_type=2'

pattern = r'\/[a-zA-Z]+\?'  # 模式字符串
stoken = re.findall(pattern, str(url), re.I)  # 匹配字符串不区分大小
stoken = stoken[0][1:-1]
url = 'http://api-api2.lemondream.cn/api/Share/get_release_content_info&share_token='+stoken
# print(url)
response = requests.get(url)
title = response.json()['data']['info']['title']
video_url = response.json()['data']['info']['video_obj']['video_url']
image_url = response.json()['data']['info']['video_obj']['url']
print('标题：',title)
print('视频地址：',video_url)
print('封面',image_url)

