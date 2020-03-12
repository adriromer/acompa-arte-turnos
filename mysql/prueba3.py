import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='127.0.0.1',
                                     database='acompadb',
                                     user='root',
                                     password='adrian')

sql_select_Query = "select terapista_id from terapistas"
cursor = connection.cursor(dictionary=True)

cursor.execute(sql_select_Query)
records = cursor.fetchall()
for row in records:
    print(row)


print("Total number of rows in terapistas is: ", cursor.rowcount)
