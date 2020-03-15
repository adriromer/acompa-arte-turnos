    def get_doctors(self):
        """trae la lista completa de terapistas."""
        connection = mysql.connector.connect(host='127.0.0.1', database='acompadb', user='root', password='adrian')
        sql_select_Query = "select * from terapistas"
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_select_Query)
        allrecords = cursor.fetchall()

#        ejemplo de for
#        print("for")
#        for row in allrecords:
#            print(row[0])
