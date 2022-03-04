import requests
import pprint
import mysql.connector
from mysql.connector import errorcode
import re

# 連線資料庫

sql_user = 'root'
sql_password = '0939856005'
DB_NAME = 'pchome'

try:
    cnx = mysql.connector.connect(user=sql_user,
                                  password=sql_password)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print('connection success')

cursor = cnx.cursor()


# 建立資料庫(若無)
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

TABLES = {}
TABLES['products'] = (
    "CREATE TABLE `products` ("
    "  `id` int NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(50) NOT NULL,"
    "  `price` int NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# 爬資料放資料 https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html


add_product = ("INSERT INTO products "
               "(name, price) "
               "VALUES (%s, %s)")

#insert ignore into 可以避免重複值

for i in range(1, 30):
    url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E6%9B%B2%E9%9D%A2%E8%9E%A2%E5%B9%95&page={}&sort=sale/dc'.format(i)
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        print(i)
        print('error', r.status_code)
        continue
    data = r.json()
    # pprint.pprint(data)
    for product in data['prods']:
        name = product['name']
        price = product['price']
        if len(name) > 50:
            name = name[:50]
        print(name)
        print(price)
        data_product = (name, price)
        # insert new product
        cursor.execute(add_product, data_product)

# 確認資料放進資料庫
cnx.commit()

print('closing')
cursor.close()
cnx.close()
