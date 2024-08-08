# Name: Brandon Castellanos
# Student ID: 011341797

import datetime
import sys
from loaddata import load_package_data
from loaddata import load_address_data
from loaddata import load_distance_data
from hashtable import Hashtable
from truck import Truck

# importing data from csv files into global variables
package_hashtable = Hashtable()
load_package_data(package_hashtable)
distance_data = []
load_distance_data(distance_data)
address_data = []
load_address_data(address_data)


# function find_address_index is used to find index from address_data matrix
def find_address_index(address_to_find):
    index = 0
    for address in address_data:
        if address_to_find == address:
            return index
        index += 1
    return -1


# function get_distance_between is used to find the distance length using address index to be used to locate
# in distance data matrix
def get_distance_between(loc_a, loc_b):
    starting_index = find_address_index(loc_a)
    destination_index = find_address_index(loc_b)

    if starting_index > destination_index:
        distance = float(distance_data[starting_index][destination_index])
    else:
        distance = float(distance_data[destination_index][starting_index])

    return distance


# function look_up returns a package properties given the package id at a suggested time
def look_up(pkg_id, cur_time):
    package = package_hashtable.search(pkg_id)
    package.set_status(package.p_id, cur_time)
    print(str(package))


def simulate_delivery(truck_obj):
    current_time = truck_obj.last_depart
    temp = []
    for package in truck_obj.truck_packages:
        temp.append(package)

    while len(temp) > 0:
        min_distance = sys.maxsize
        closest_distance_package = None

        # determining closest package from truck
        for p_id in temp:
            package = package_hashtable.search(p_id)
            package.truck_num = truck_obj.truck_number
            package.departed_time = truck_obj.last_depart
            distance = get_distance_between(truck_obj.current_address, package.address)
            if distance <= min_distance:
                min_distance = distance
                closest_distance_package = package

        # updating package properties
        truck_obj.current_address = closest_distance_package.address
        truck_obj.miles_traveled += min_distance

        # calculating time elapsed to the closest package location
        current_time += datetime.timedelta(hours=min_distance/18)
        closest_distance_package.delivery_time = current_time
        # removing package from manifest
        temp.remove(closest_distance_package.p_id)


# Assigning packages manually
t1_list = [1, 13, 5, 14, 15, 16, 19, 20, 29, 30, 31, 37, 40]
t2_list = [2, 3, 4, 7, 8, 18, 6, 25, 32, 34, 28, 36, 38]
t3_list = [9, 10, 11, 12, 17, 21, 35, 22, 23, 24, 26, 27, 33, 39]

# truck departing at 8:00am
truck_1 = Truck(1, t1_list, last_depart=datetime.timedelta(hours=8))
simulate_delivery(truck_1)

# truck departing at 9:10am
truck_2 = Truck(2, t2_list, last_depart=datetime.timedelta(hours=9, minutes=10))
simulate_delivery(truck_2)

# truck departing at 10:30am
truck_3 = Truck(3, t3_list, last_depart=datetime.timedelta(hours=10, minutes=30))
simulate_delivery(truck_3)


# function is used to receive time input from user in the form of HH:MM
def get_time_input():
    time = input('Enter a time in the 24-hour format HH:MM \n')
    h, m = map(int, time.split(':'))
    res = datetime.timedelta(hours=h, minutes=m)
    return res


while True:
    print("****** Western Governors University Package Service ******")
    print("\nSelect an option below to view more info: \n")
    print("1: Print All Package Status and Total Mileage.")
    print("2: Get a Single Package Status with a Time.")
    print("3: Get All Package Status with a Time")
    print("4: Exit the Program")

    choice = input("Select an option: ")

    # Displaying all package status and total miles traveled for each truck
    if choice == "1":
        print()
        print("Truck 1: %0.2f miles traveled. " % float(truck_1.miles_traveled))
        print()
        for p_id in truck_1.truck_packages:
            look_up(p_id, datetime.timedelta(hours=17))
        print()

        print("Truck 2: %0.2f miles traveled. " % float(truck_2.miles_traveled))
        print()
        for p_id in truck_2.truck_packages:
            look_up(p_id, datetime.timedelta(hours=17))
        print()

        print("Truck 3: %0.2f miles traveled. " % float(truck_3.miles_traveled))
        print()
        for p_id in truck_3.truck_packages:
            look_up(p_id, datetime.timedelta(hours=17))
        print()

        print("Total mileage used: %.2f" % (truck_1.miles_traveled + truck_2.miles_traveled + truck_3.miles_traveled))

    # Displaying a single package with a user suggested time
    elif choice == "2":

        package_id = int(input("Enter package id:"))
        p = package_hashtable.search(package_id)
        user_time = get_time_input()
        look_up(p.p_id, user_time)
        print()

    # Displaying all package status with a user suggested time
    elif choice == "3":
        user_time = get_time_input()
        for p_id in range(1, 41):
            p = package_hashtable.search(p_id)
            look_up(p_id, user_time)
        print()

    # Exiting program
    elif choice == "4":
        exit()
