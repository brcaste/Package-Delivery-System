# Name: Brandon Castellanos
# Student ID: 011341797

import csv
from package import Package


def load_package_data(package_hashtable):
    with open('Data/PackageFile_raw.csv', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            p_id = int(row[0])
            p_address = row[1]
            p_city = row[2]
            p_state = row[3]
            p_zip = row[4]
            p_deadline = row[5]
            p_weight = row[6]
            package = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight)
            package_hashtable.insert(p_id, package)


def load_distance_data(distance_list):
    with open('Data/DistancesFile_raw.csv', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            distance_list.append(row)


def load_address_data(address_list):
    with open('Data/Addresses.csv', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            address_list.append(row[0])
