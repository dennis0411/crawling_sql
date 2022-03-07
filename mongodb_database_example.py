import requests
import pprint
from pymongo import MongoClient

# 建立實例

client = MongoClient()
db = client.pchome
coll = db.products

# 抓資料


for i in range(1, 30):
    url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E6%9B%B2%E9%9D%A2%E8%9E%A2%E5%B9%95&page={}&sort=sale/dc'.format(
        i)
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        print(i)
        print('error', r.status_code)
        continue

    data = r.json()

    # 直接加入資料
    for product in data['prods']:
        coll.insert_one(product)




