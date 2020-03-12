import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='acompadb',
                                         user='root',
                                         password='adrian')

    sql_select_Query = "select * from terapistas"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_select_Query)

    print("\nPrinting each terapistas record")
    for row in cursor:
        print("* {Name}".format(Name=row['Name']



except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")