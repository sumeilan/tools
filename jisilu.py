import requests,json
import re
def get_fund_id(datas,select_id):
    fund = [('基金代码','基金名称','现价','溢价率')]
    for i in datas:
        QDII = i
        if QDII['id'] == str(select_id):
            d_QDII = QDII['cell']['fund_id'],QDII['cell']['fund_nm'],QDII['cell']['price'],QDII['cell']['discount_rt']
            fund.append(d_QDII)
    print(fund)


#QDII
response = requests.get('https://www.jisilu.cn/data/qdii/qdii_list/?___jsl=LST___t=1582859926238&rp=25&page=1')
j_data = json.loads(response.text)
print(get_fund_id(j_data['rows'],162411))


