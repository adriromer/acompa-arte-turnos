'''This module stores doctor data and provides methods for GET, POST and DELETE calls.
'''
from random import randint
import mysql.connector

class DoctorData(object):

    def __init__(self):

        self.doctors = (self.get_doctors())  # Key: terapista_id Value: DoctorInfo()
        print("dictionario self.doctors toda la  informacion de  los doctores")
        print(self.doctors)


    def get_doctors(self):
        """trae la lista completa de terapistas."""
        connection = mysql.connector.connect(host='127.0.0.1', database='acompadb', user='root', password='adrian')
        sql_select_Query = "select * from terapistas"
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_select_Query)
        allrecords = cursor.fetchall()


        return [{row[0]: {"first_name": row[1], "last_name": row[2], "status": row[3]}} for row in
                allrecords]

    def add_appointment(self, json_data,):
        """ agrega un nuevo turno. """
        connection = mysql.connector.connect(host='127.0.0.1', database='acompadb', user='root', password='adrian')
        sql_select_Query = "select terapista_id from terapistas"
        cursor = connection.cursor(buffered=True, dictionary=True)
        cursor.execute(sql_select_Query)
        self.allrecords = cursor.fetchall()
        #allrecords trae todos los terapistasid [{'terapista_id': 129}, {'terapista_id': 203}, {'terapista_id': 435}]


        self.terapista_idjson = int(json_data['terapista_id'])
        #sef.terapista_idjson trae el id del terapista que se envio

        self.all_terpista_id = []
        for value in self.allrecords:
            self.all_terpista_id.append(value['terapista_id'])

        if self.terapista_idjson not in self.all_terpista_id:
            raise KeyError("Invalid terapista_id.")


        # validado que el doctor existe en la base, parseo todos los datos del json para agregar el turno

        insert_apt = ("INSERT INTO appointment "
                           "(apt_id, date, time, patient_id, terapista_id) "
                           "VALUES (%s, %s, %s, %s, %s)")

        self.apt_data = [json_data["apt_id"],
                    json_data["date"],
                    json_data["time"],
                    json_data["patient_id"],
                    json_data["terapista_id"]]

        print("ejecuto el insert")
        try:
            cursor.execute(insert_apt, self.apt_data)
            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))

        return "turno registrado"


    def get_appointments(self, terapista_id, date):
        """ Returns all appointments of a doctor for a given date."""
        if terapista_id not in self.doctors:
            raise KeyError("Invalid Doc_ID")
        doctor = self.doctors[int(doc_id)]
        appointments = doctor.get_appointments(date)
        return [{str(appointment[0]): str(appointment[1])} for appointment in appointments.items()]

    def del_appointment(self, doc_id, date, apt_id):
        """ Deletes an appointment specified by doctor id, appointment id and date"""
        if doc_id not in self.doctors:
            raise KeyError("Invalid Doc_ID")
        doctor = self.doctors[int(doc_id)]
        return doctor.del_appointment(date, apt_id)


class DoctorInfo(object):
    """Class holds all the data of a doctor.

    This class hold all the doctor data as DoctorInfo() objects.

    Attributes:
        first_name: Doctor first name.
        last_name: Doctor last name.
        dates: all the dates the doctor has appointments.
        get_appointment: A function to return all appointments for a given date.
        del_appointment: A function to delete an appointment.
    """

    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name
        self.dates = dict()  # Key: Date Value: DateInfo()

#    def add_appointment(self, date, time, apt_id, apt_data):
        '''
        Retrieve Date Info for the particular date for the doctor and add appointment
        '''

#        print(self.first_name)
#        print(self.last_name)
#        print(self.dates)
#
#        if date not in self.dates:
#            self.dates[date] = DateInfo()
#        date_info = self.dates[date]
#        return date_info.add_appointment(time, apt_id, apt_data)

    def get_appointments(self, date):
        """ Returns all appointment of the given date."""
        if date not in self.dates:
            raise KeyError("Not a valid date")
        return self.dates[date].appointments

    def del_appointment(self, date, apt_id):
        """ Deletes an appointment for the given date"""

        if date not in self.dates:
            raise KeyError("Given appointment date doesn't exist")
        date_info = self.dates[date]
        return date_info.del_appointment(apt_id)


class DateInfo(object):
    """Class holds all the data of a particular date.

    Attributes:
        appointments: All the appointments. Key: Appointment_ID Value: Appointment()
        booked: A dict() that keeps track of booked slots. Assuming GUI provides a fixed
                set of slots (Example: Every hour)
        dates: all the dates the doctor has appointments.
        add_appointment: A function to add a new appointment.
        del_appointment: A function to delete an appointment.
    """

    def __init__(self):
        self.appointments = dict()  # Key: Appointment_ID Value: Appointment()
        self.booked = dict()  # Key: Time Value: True

    def __str__(self):
        return str([str(appointment) for appointment in self.appointments.items()]) + str(self.booked.items())

#    def add_appointment(self, time, apt_id, apt_data):
#        """ Adds an appointment. """
#        if time in self.booked:
#            raise ValueError("The slot is already booked.")
#        self.booked[time] = True
#        self.appointments[int(apt_id)] = Appointment(*apt_data)
#        return "Appointment booked."

    def del_appointment(self, apt_id):
        """ Deletes an appoint. """
        if apt_id not in self.appointments:
            raise KeyError("No such appointment to delete.")
        apt_time = self.appointments[int(apt_id)].time
        del self.appointments[int(apt_id)]
        del self.booked[apt_time]
        return "Appointment deleted."


class Appointment(object):
    """Class holds all the data of an appointment. """

    def __init__(self, patient_first_name, patient_last_name, date, time, kind):
        self.patient_first_name = patient_first_name
        self.patient_last_name = patient_last_name
        self.date = date
        self.time = time
        self.kind = kind

    def __str__(self):
        return str(self.__dict__)