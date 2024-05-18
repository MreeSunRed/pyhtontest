import requests
from bs4 import BeautifulSoup
URL = 'http://127.0.0.1:5500/day4/03promise%E8%A7%A3%E5%86%B3%E5%9B%9E%E8%B0%83%E5%9C%B0%E7%8B%B1.html'
#在字典headers中添加Cookie这一项。
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        }
wb_data = requests.get(URL, headers=headers)
soup = BeautifulSoup(wb_data.content, 'html.parser')
print(soup.select('body > select:nth-child(1) > option.province'))
