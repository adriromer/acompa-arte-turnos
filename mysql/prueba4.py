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


def get_doctors(self):
    """Retrieves list of all doctors."""

    print([{doc[0]: {"first_name": doc[1].first_name, "last_name": doc[1].last_name}} for doc in
           self.doctors.items()])
    print(self.doctors.items())

    return [{doc[0]: {"first_name": doc[1].first_name, "last_name": doc[1].last_name}} for doc in
            self.doctors.items()]


