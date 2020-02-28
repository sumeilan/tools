import requests,json,time
from tkinter import *
import tkinter.messagebox
class fund:
    def __init__(self):
        self.mstime = int(round(time.time() * 1000))
        self.host = 'https://www.jisilu.cn/data/'

    def get_fund_id(self,datas, ids):
        fund = []
        for i in datas:
            QDII = i
            for i in ids:
                if QDII['id'] == str(i):
                    d_QDII = QDII['cell']['fund_id'], QDII['cell']['fund_nm'], QDII['cell']['price'], QDII['cell'][
                        'fund_nav'], QDII['cell']['estimate_value'], QDII['cell']['discount_rt']
                    fund.append(d_QDII)
        return fund

    def get_QDII(self,fund_ids):
        fund = [('QDII基金代码', '基金名称', '现价', '净值', '最新估值', '溢价率')]
        path  = 'qdii/qdii_list/?___jsl=LST___t= '
        url = self.host + path + str(self.mstime)
        response = requests.get(url)
        # print(response.text)
        datas = json.loads(response.text)
        QDII_fund = self.get_fund_id(datas['rows'], fund_ids)
        return fund + QDII_fund

    def get_ETF(self,fund_ids):
        fund = [('ETF基金代码', '基金名称', '现价', '净值', '最新估值', '溢价率')]
        path = 'etf/etf_list/?___jsl=LST___t='
        url = self.host + path + str(self.mstime)
        response = requests.get(url)
        datas = json.loads(response.text)
        QDII_fund = self.get_fund_id(datas['rows'], fund_ids)
        return fund + QDII_fund

    def show_fund(self,*fund):
        for l in fund:
            for k in l:
                print(k)
            print('\n')

F = fund()
qdii_fund_ids =[162411, 159920, 513520,160416]
etf_fund_ids =  [512580, 512980, 512880,515180,510300,510510,159938]
QDII_fund = F.get_QDII(qdii_fund_ids)
ETF_fund = F.get_ETF(etf_fund_ids)
F.show_fund(QDII_fund,ETF_fund)
