import os
import json

folder_count = 0
input_path = "out"

for folders in os.listdir(input_path):
    folder_count += 1

def get_volunteer_information(folder_count):
    volunteer_id = folder_count + 1
    preferred_name = str(input("Enter Preferred Name -> "))
    passport_name = str(input("Enter Passport Name -> "))
    phone_number = int(input("Enter Phone Number -> "))
    email = str(input("Enter Email -> "))
    wechat_id = str(input("Enter Wechat ID -> "))
    nationality = str(input("Enter Nationality -> "))
    school_name = str(input("Enter School Name -> "))
    date_of_birth = str(input("Enter your Date of Birth -> "))
    graduation = str(input("Enter your Graduation Year -> "))
    os.system("cls")
    create_folder_and_json_file(volunteer_id, preferred_name, passport_name, phone_number, email, wechat_id, nationality, school_name, date_of_birth, graduation)

def create_folder_and_json_file(volunteer_id, preferred_name, passport_name, phone_number, email, wechat_id, nationality, school_name, date_of_birth, graduation):
    os.makedirs(input_path + "/" + str(volunteer_id))
    folder_path = input_path + "/" + str(volunteer_id)
    json_path = folder_path + "/general_data.json"

    json_data = {
        "Volunteer_ID": volunteer_id,
        "Preferred_Name" : preferred_name,
        "Passport_Name" : passport_name,
        "Phone_Number" : phone_number,
        "Email" : email,
        "Wechat_ID" : wechat_id,
        "Nationality" : nationality,
        "School" : school_name,
        "Date of Birth" : date_of_birth,
        "Graduation" : graduation
    }

    with open(json_path, 'w') as f:
        json.dump(json_data, f, indent=2)

get_volunteer_information(folder_count)