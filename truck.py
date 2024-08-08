# Name: Brandon Castellanos
# Student ID: 011341797

def load_truck_packages(package_id_list, package_hashtable):
    package_list = []
    for p_id in package_id_list:
        p_id = int(p_id)
        package_hashtable.find(p_id).status = "En Route"
        package_list.append(package_hashtable.find(p_id))
    return package_list


class Truck:

    def __init__(self, truck_number, truck_packages, last_depart):
        self.truck_number = truck_number
        self.truck_packages = truck_packages
        self.miles_traveled = 0
        self.current_address = "4001 South 700 East"
        self.last_depart = last_depart

    def __str__(self):
        return 'Truck #: %s, Miles Traveled: %s, Current Address: %s, Time Left Hub: %s' % (self.truck_number, self.miles_traveled, self.current_address, self.last_depart)

