# Name: Brandon Castellanos
# Student ID: 011341797
import datetime


class Package:
    def __init__(self, p_id, address, city, state, zipcode, deadline, weight):
        self.p_id = p_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = "At Hub"
        self.delivery_time = ""
        self.departed_time = ""
        self.truck_num = ""

    def set_status(self, p_id, cur_time):
        if p_id == 9:
            self.package_update(9, cur_time)

        if cur_time > self.departed_time and cur_time >= self.delivery_time:
            self.status = 'Delivered'

        elif cur_time < self.departed_time:
            self.status = 'At Hub'
        else:
            self.status = 'En Route'

    def package_update(self, p_id, cur_time):

        if p_id == 9 and cur_time > datetime.timedelta(hours=10, minutes=20):
            self.address = '410 S State St'
            self.city = 'Salt Lake City'
            self.state = 'UT'
            self.zipcode = '84111'
        else:
            self.address = '300 State St'
            self.city = 'Salt Lake City'
            self.state = 'UT'
            self.zipcode = '84103'

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "ID: %s, Address: %s, %s, %s, %s, Deadline: %s, Weight: %s kg, Time Delivered: %s, Time Departed: %s, Status: %s, By Truck #:%s" % (self.p_id, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.delivery_time, self.departed_time, self.status, self.truck_num)

