import requests,json,time
from tkinter import *
import tkinter.messagebox

url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=5687069307&containerid=1076035687069307'
response = requests.get(url)
datas = json.loads(response.text)
cards = datas['data']['cards']
print('E大weibo：')
k = 0
for i in cards:
    if k > 0:
        print( str(k) + '、'+i['mblog']['text']+ '\n')
    k = k +1