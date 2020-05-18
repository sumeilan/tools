import requests,json,time
from tkinter import *
import tkinter.messagebox
class fund:
    def __init__(self):
        self.mstime = int(round(time.time() * 1000))
        self.host = 'https://www.jisilu.cn/data/'
        #https://www.jisilu.cn/data/qdii/qdii_list/A?___jsl=LST___t=1587358090721&rp=22&page=1
        self.C_qdii_path  = 'qdii/qdii_list/C?___jsl=LST___t='
        self.E_qdii_path = 'qdii/qdii_list/E?___jsl=LST___t='
        self.A_qdii_path = 'qdii/qdii_list/A?___jsl=LST___t='

        self.etf_path = 'etf/etf_list/?___jsl=LST___t='
        self.name = ('基金代码', '基金名称', '现价','涨幅', '净值', '最新估值', '溢价率')

    def get_fund_id(self,datas, ids):
        fund = []
        for i in datas:
            QDII = i
            for i in ids:
                if QDII['id'] == str(i):
                    d_QDII = QDII['cell']['fund_id'], QDII['cell']['fund_nm'], QDII['cell']['price'],QDII['cell']['increase_rt'],QDII['cell'][
                        'fund_nav'], QDII['cell']['estimate_value'], QDII['cell']['discount_rt']
                    fund.append(d_QDII)
        return fund

    def get_C_QDII(self,fund_ids):
        url = self.host + self.C_qdii_path + str(self.mstime)
        response = requests.get(url)
        datas = json.loads(response.text)
        C_QDII_fund = self.get_fund_id(datas['rows'], fund_ids)
        return C_QDII_fund

    def get_A_QDII(self,fund_ids):
        url = self.host + self.A_qdii_path + str(self.mstime)
        response = requests.get(url)
        datas = json.loads(response.text)
        A_QDII_fund = self.get_fund_id(datas['rows'], fund_ids)
        return A_QDII_fund

    def get_E_QDII(self,fund_ids):
        url = self.host + self.E_qdii_path + str(self.mstime)
        response = requests.get(url)
        datas = json.loads(response.text)
        E_QDII_fund = self.get_fund_id(datas['rows'], fund_ids)
        return E_QDII_fund

    def get_ETF(self,fund_ids):
        url = self.host + self.etf_path + str(self.mstime)
        response = requests.get(url)
        datas = json.loads(response.text)
        QDII_fund = self.get_fund_id(datas['rows'], fund_ids)
        return QDII_fund

    def my_fund(self,fund_ids):
        my_cqdii = self.get_C_QDII(fund_ids)
        my_eqdii = self.get_E_QDII(fund_ids)
        my_aqdii = self.get_A_QDII(fund_ids)
        my_etf = self.get_ETF(fund_ids)
        self.show_fund(my_cqdii,my_aqdii,my_eqdii,my_etf)

    def show_fund(self,*fund):
        print(self.name)
        for l in fund:
            for k in l:
                print(k)


F = fund()
qdii_fund_ids =[162411, 159920, 513520,160416,513030,501018]
etf_fund_ids =  [512580, 512980, 512880,515180,510510,159938,159940]
my_fund = [510300,510500,513500,513100]
C_QDII_fund = F.get_C_QDII(qdii_fund_ids)
E_QDII_fund = F.get_E_QDII(qdii_fund_ids)
A_QDII_fund = F.get_A_QDII(qdii_fund_ids)

ETF_fund = F.get_ETF(etf_fund_ids)
F.show_fund(A_QDII_fund,C_QDII_fund,E_QDII_fund,ETF_fund)
print('\n')
F.my_fund(my_fund)