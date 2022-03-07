import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='0939856005',
                              database='pchome',
                              host='127.0.0.1')
cursor = cnx.cursor(dictionary=True)

query = ("SELECT * FROM products "
         "WHERE name LIKE '%ASUS%' AND price > 5000")


cursor.execute(query)

for row in cursor:
  print(row['name'])

cursor.close()
cnx.close()

