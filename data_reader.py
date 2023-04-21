# room number, number of beds, availabilty, charges per day, name of applicant, age, address
import csv

file = open("Hotel_Data.csv", "r")
list_file = list(csv.reader(file))
file.close()

room_numbers_list = []
for i in range(len(list_file)):
    room_numbers_list.append(list_file[i][0])

number_of_beds = []
for i in range(len(list_file)):
    number_of_beds.append(int(list_file[i][1]))

availability = []
for i in range(len(list_file)):
    availability.append(int(list_file[i][2]))

charges_per_day = []
for i in range(len(list_file)):
    charges_per_day.append(int(list_file[i][3]))

name_of_applicant = []
for i in range(len(list_file)):
    name_of_applicant.append(list_file[i][4])

age = []
for i in range(len(list_file)):
    if list_file[i][5].isnumeric is True:
        age.append(int(list_file[i][5]))
    else:
        age.append(list_file[i][5])

address = []
for i in range(len(list_file)):
    address.append(list_file[i][6])

'''print("room no: ", room_numbers_list)
print("no. of beds: ", number_of_beds)
print("availability: ", availability)
print("charge: ", charges_per_day)
print("name: ", name_of_applicant)
print("age: ", age)
print("address:  ", address)'''
