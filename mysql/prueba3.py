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

##################################################################################################################
#popula
##################################################################################################################

def populate_doctorid_from_db(self):
    connection = mysql.connector.connect(host='127.0.0.1', database='acompadb', user='root', password='adrian')
    sql_select_Query = "select terapista_id from terapistas"
    cursor = connection.cursor(buffered=True)
    cursor.execute(sql_select_Query)
    ids = []
    allrecords = cursor.fetchall()
    for i in allrecords:
        k = list(i)
        ids.append(k[0])
    return ids

    def add_doctor(self, first_name, last_name):
        """Adds new doctor to to doctors dict() with a unique id. """
        doc_id = str(self.populate_doctorid_from_db())
        self.doctors[doc_id] = DoctorInfo(first_name, last_name)
