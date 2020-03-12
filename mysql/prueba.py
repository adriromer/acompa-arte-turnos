

import mysql.connector
from mysql.connector import Error

doctors = dict()
doc_id = (1)
doc_id2 = (2)

#el dictionario vacio se llama doctors, con la funcion de abajo le agrega la key ( [doc_id] ) y el valor
doctors[doc_id] = "pepe"
doctors[doc_id2] = "pepe"

print(doctors)


#####################################################################################################################
#ejemplo de conexion a db mysql

''' 
try:
    connection = mysql.connector.connect(host='127.0.0.1',
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

'''
################################################################################
# conexion a db con un select
################################################################################

try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='acompadb',
                                         user='root',
                                         password='adrian')

    sql_select_Query = "select * from terapistas"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in terapistas is: ", cursor.rowcount)

    print("\nPrinting each terapistas record")
    for row in records:
        print("terapista_id = ", row[0], )
        print("primer_nombre = ", row[1])


except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")

