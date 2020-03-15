
from random import randint


def add_doctor(first_name, last_name):
    """Adds new doctor to to doctors dict() with a unique id. """
    doc_id = randint(1, 9999)
    doctors[doc_id] = DoctorInfo(first_name, last_name)



class DoctorInfo(object):


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.dates = dict() # Key: Date Value: DateInfo()

    def add_appointment(self, date, time, apt_id, apt_data):
        '''
        Retrieve Date Info for the particular date for the doctor and add appointment
        '''
        if date not in self.dates:
            self.dates[date] = DateInfo()
        date_info = self.dates[date]
        return date_info.add_appointment(time, apt_id, apt_data)

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





doctors = dict() # Key: Doc_ID Value: DoctorInfo()
add_doctor('John', 'Doe')
add_doctor('Jane', 'Doe')

print(doctors)