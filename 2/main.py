import json
import time

from bs4 import BeautifulSoup as bs
import requests as rs
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
}
url='https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=zb&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22reg%22%2C%22valuecode%22%3A%22110000%22%7D%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A050I%22%7D%5D&k1=1716024876156&h=1'
def listMake(url):#输入ajax请求地址可从国家统计局获取数据返回列表
    r = rs.get(url, headers=header)
    r.encoding = 'utf-8'
    soup = bs(r.text, 'html.parser')
    js = json.loads(str(soup))
    list = []
    print(js['returndata']['datanodes'][1]['data']['data'])  # 最终数据
    for i in range(1, 10):
        list.append(js['returndata']['datanodes'][i]['data']['data'])  # 制成列表
    return list

list = listMake(url)
import numpy as np
year = np.arange(2014,2023)
#制成图表
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.plot(year,list,label='北京',marker = "o")
plt.xlabel('年份')
plt.ylabel('房价销售额(亿)')

#上海
url='https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=zb&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22reg%22%2C%22valuecode%22%3A%22310000%22%7D%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A050I%22%7D%5D&k1=1716026686850&h=1'
list = listMake(url)
plt.plot(year,list,label='上海',marker = "x")

#天津
url='https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=zb&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22reg%22%2C%22valuecode%22%3A%22120000%22%7D%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A050I%22%7D%5D&k1=1716026857687&h=1'
list = listMake(url)
plt.plot(year,list,label='天津',marker = "o")

plt.legend()
plt.grid()
# plt.show()
plt.savefig(r'房价销售情况.svg')
