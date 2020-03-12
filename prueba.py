
from flask import json
from flask import request
import mysql.connector
from mysql.connector import Error

doctors = dict()
doc_id = (1)
doc_id2 = (2)

#el dictionario vacio se llama doctors, con la funcion de abajo le agrega la key ( [doc_id] ) y el valor
doctors[doc_id] = "pepe"
doctors[doc_id2] = "pepe"

print(doctors)

response = request.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)


#####################################################################################################################
#ejemplo de conexion a db mysql

try:
    connection = mysql.connector.connect(host='192.168.0.118',
                                         database='acompadb',
                                         user='root',
                                         password='adrian')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")