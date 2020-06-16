import numpy as np
from math import e
import math


#Score=Log10000（当日表态好的记录数量） + 内容发布（或入库）时间距离2019.7.1的时间间隔（单位分钟）/10
x = 1590650590  #内容发布的时间戳
y = 1588059112  #内容发布的时间戳
score = math.log(2,10000) + (int(x)-int(1561910400))/60/10
score1 = math.log(2,10000) + (int(y)-int(1561910400))/60/10

# print(math.log(2,10000))   #log10000为底

scor = math.log(5,e)
print(2/scor)   #log10000为底