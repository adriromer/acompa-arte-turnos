from random import randint


doctors-prueba = dict({423: {'first_name': 'emanuel', 'last_name': 'rolon'}})

def get_keys():
    for item in my_dict:
        print(item, "tiene el valor:", my_dict[item])


def prueba():
    return [{doc[0]: {"first_name": doc[1].first_name, "last_name": doc[1].last_name}} for doc in
            doctors.items()]


doctors = dict()

read_dbterapistas()


def read_dbterapistas(first_name, last_name):
   """Adds new doctor to to doctors dict() with a unique id. """
    doc_id = randint(1, 999)
    self.doctors[doc_id] = DoctorInfo(first_name, last_name)



