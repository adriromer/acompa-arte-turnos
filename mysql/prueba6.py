import mysql.connector

def get_doctor():
    connection = mysql.connector.connect(host='127.0.0.1', database='acompadb', user='root', password='adrian')
    sql_select_Query = "select * from terapistas"
    cursor = connection.cursor(buffered=True)
    cursor.execute(sql_select_Query)
    allrecords = cursor.fetchall()
    for row in allrecords:
        print("Doctor_Id = ", row[0])
        print("First_Name = ", row[1])
        print("last_Name  = ", row[2])
        print("status  = ", row[3], "\n")
    for allrow in allrecords:
        print(allrow)

    return [{row[0]: {"first_name": row[1], "last_name": row[2], "status": row[3]}} for row in
            allrecords]


print(get_doctor_ids())