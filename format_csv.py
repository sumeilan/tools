import pandas as pd
import csv ,os

filename = 'D:\\JMeter\\work\\duid.csv'
file1 = 'D:\\JMeter\\work\\duid2.csv'
data = pd.read_csv(filename)
# data_new = data.drop([1,5])#删除第一和第五行
#data_new=data.drop(["title"],axis=1) #删除title这列数据
data_new = data.drop(range(10)) #删除前10行
data_new.to_csv(file1,index=0)

