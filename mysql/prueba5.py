import mysql.connector

def get_doctor_ids():
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='acompadb',
                                         user='root',
                                         password='adrian')

    sql_select_Query = "select terapista_id from terapistas"
    cursor = connection.cursor(buffered=True)
    cursor.execute(sql_select_Query)
    ids = []
    allrecords = cursor.fetchall()
    for i in allrecords:
        k = list(i)
        ids.append(k[0])
    return ids

ids = tuple(get_doctor_ids())
print(ids)