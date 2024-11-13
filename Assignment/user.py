#Imports the JSON library
import json

class User:
    #Defines the parameters and their type (note: phone number is a string)
    def __init__(self, age: int, city: str, first_name: str, last_name: str, id: int, phone_number: str):
        self.__age = age
        self.__city = city
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id = id
        self.__phone_number = phone_number

    #Gets/sets user age
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    #Gets/sets user city
    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    #Gets/sets user first name
    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    #Gets/sets user last name
    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    #Gets/sets user ID
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    #Gets/sets user phone number
    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    #Converts JSON objects into Python class objects
    def from_json(data_set):
        return User(int(data_set["age"]), data_set["city"], data_set["first_name"], data_set ["last_name"], int(data_set["id"]), data_set["phone_number"])

    #Formats to a string
    def __str__(self):
        return f"Age: {self.__age}\nCity: {self.__city}\nFirst Name: {self.__first_name}\nLast Name: {self.__last_name}\nID: {self.__id}\nPhone Number: {self.__phone_number}"

    #Additional method to get user info
    def get_user_info(self):
        return self.__str__()

    #Prints the data in a pretty format in the terminal while maintaining the format from the original JSON file
    def print_pretty(user_data):
        for user in user_data:
            print(f"\nUser ID: {user.get_id()}")
            print(f"First Name: {user.get_first_name()}")
            print(f"Last Name: {user.get_last_name()}")
            print(f"Age: {user.get_age()}")
            print(f"City: {user.get_city()}")
            print(f"Phone Number: {user.get_phone_number()}")
            print("-----------------")

    #Writes out a list of user data to a JSON file
    def write_out_json(user_data, file_name):
        writeout = [user.to_dict() for user in user_data]
        with open(file_name, "w") as file:
            json.dump(writeout, file, indent=4)

    #Converts the User object to a dictionary (for JSON serialization)
    def to_dict(self):
        return {
            "id": self.__id,
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "age": self.__age,
            "city": self.__city,
            "phone_number": self.__phone_number
        }

    #Checks if age is within a given range
    def age_in_range(self, min_age, max_age):
        return min_age <= self.__age <= max_age

    #Checks if ID is within a given range
    def id_in_range(self, min_id, max_id):
        return min_id <= self.__id <= max_id