import copy
import data_reader


number_of_persons = int(input("Number of persons: "))
name_of_applicant = input("Name: ")
age = int(input("Age: "))
address = input("Address: ")
if number_of_persons == 1 or 2 or 3:
    t = 1
    number_of_persons2 = copy.copy(number_of_persons)
if number_of_persons == 4 or 5 or 6:
    t = 1
    number_of_persons2 = 6
if number_of_persons > 6:
    t = 0
    print("no such type of room available")

if t == 1:
    number_increment1 = 0
    while number_increment1 < len(data_reader.room_numbers_list):
        if data_reader.number_of_beds[number_increment1] == number_of_persons2:
            if data_reader.availability[number_increment1] == 1:
                data_reader.availability[number_increment1] = 0
                data_reader.name_of_applicant[number_increment1] = name_of_applicant
                data_reader.age[number_increment1] = age
                data_reader.address[number_increment1] = address
                break
        number_increment1 += 1

    data_file = open("Hotel_Data.csv", "w")
    for number_increment2 in range(len(data_reader.room_numbers_list)):
        data_file.write(str(data_reader.room_numbers_list[number_increment2]) + "," + str(data_reader.number_of_beds[number_increment2]) + "," + str(data_reader.availability[number_increment2]) + "," + str(data_reader.charges_per_day[number_increment2]) + "," + str(data_reader.name_of_applicant[number_increment2]) + "," + str(data_reader.age[number_increment2]) + "," + str(data_reader.address[number_increment2]) + "\n")
    data_file.close()
    print("booking done")
    for i in range(len(data_reader.room_numbers_list)):
        if data_reader.name_of_applicant[i] == name_of_applicant:
            if data_reader.age[i] == age:
                if data_reader.address[i] == address:
                    print("Your Room No. is", data_reader.room_numbers_list[i])
