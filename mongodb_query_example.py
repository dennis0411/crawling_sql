import requests
import pprint
from pymongo import MongoClient

# 建立實例

client = MongoClient()
db = client.pchome
coll = db.products

# CRUD Practice

# query1 : 基本搜尋
# data = coll.find()
# for d in data:
#     print(d['name'])

# query2 : regex, name contains ASUS
# data = coll.find({'name': {'$regex': '.*ASUS.*'}})
# for d in data:
#     print(d['name'])

# query3 : comparison operator
# data = coll.find({'price': {'$gt' : 3000}})
# for d in data:
#     print(d['name'], d['price'])

# query4 : and comparison operator with list, asus and price greater than 3000
# data = coll.find({'$and': [{'name': {'$regex': '.*ASUS.*'}}, {'price': {'$gt': 3000}}]})
# for d in data:
#     print(d['name'], d['price'])


# update1 : format for update data

# data = coll.find_one({'name': 'ASUS XG35VQ(低藍光+不閃屏)'})
# print(data['name'], data['price'])
#
# coll.update_one({'name': 'ASUS XG35VQ(低藍光+不閃屏)'}, {'$set': {'price': 8000}})
#
# data = coll.find_one({'name': 'ASUS XG35VQ(低藍光+不閃屏)'})
# print(data['name'], data['price'])


# update2 : insert if not exist using upsert
# coll.update_one({'name': 'APPLE'}, {'$set': {'name': 'APPLE'}}, upsert= True)

# delete : delete data
# coll.delete_one({'name': 'APPLE'})
