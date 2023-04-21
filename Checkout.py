import data_reader

room_number_input = input("Room No.: ")
k = 0
l = 0
if room_number_input in data_reader.room_numbers_list:
    for number_increment3 in range(len(data_reader.room_numbers_list)):
        if data_reader.room_numbers_list[number_increment3] == room_number_input:
            if len(data_reader.name_of_applicant[number_increment3]) > 0:
                print("Name:", data_reader.name_of_applicant[number_increment3])
                print("Age:", data_reader.age[number_increment3])
                print("Address:", data_reader.address[number_increment3])
                key_confirmation = input("confirmation (yes or no): ")
                if key_confirmation == "yes":
                    data_reader.availability[number_increment3] = 1
                    data_reader.name_of_applicant[number_increment3] = ""
                    data_reader.age[number_increment3] = ""
                    data_reader.address[number_increment3] = ""
                    print("Checkout Confirmed")
                    break
                else:
                    print("Checkout cancelled")
                    break
            k += 1
    if k > 0:
        print("Room is not booked")
else:
    print("Wrong room number")

data_file = open("Hotel_Data.csv", "w")
for number_increment4 in range(len(data_reader.room_numbers_list)):
    data_file.write(str(data_reader.room_numbers_list[number_increment4]) + "," + str(data_reader.number_of_beds[number_increment4]) + "," + str(data_reader.availability[number_increment4]) + "," + str(data_reader.charges_per_day[number_increment4]) + "," + str(data_reader.name_of_applicant[number_increment4]) + "," + str(data_reader.age[number_increment4]) + "," + str(data_reader.address[number_increment4]) + "\n")
data_file.close()
