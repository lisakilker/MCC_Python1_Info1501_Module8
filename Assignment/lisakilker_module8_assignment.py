#Imports libraries
import json
import os
#Imports the User class from user.py
from user import User

#Lists the JSON files available in the directory
def list_json_files():
    return [f for f in os.listdir() if f.lower().endswith(".json")]

def main():
    #Prints the current working directory
    print(f"Current working directory: {os.getcwd()}")
    #Prints all files in the directory
    print(f"Files in directory: {os.listdir()}")
    
    #Allows the user to search for the main data file in the directory
    while True:
        file_name = input("\nWhat's the name of the file that you'd like to search through?: ").strip()
        if not file_name:
            file_name = "data.json"
        elif not file_name.lower().endswith(".json"):
            file_name += ".json"

        if os.path.exists(file_name):
            #Prints that the file was found
            print("\nFile found!")
            break
        else:
            #If the user enters an invalid file name, this will give the user a list of the available files to choose from
            print(f"\nThe file '{file_name}' does not exist. Here are the available files:")
            json_files = list_json_files()
            if json_files:
                print("\n".join(json_files))
            else:
                print("\nNo JSON files found in the current directory.")

    user_data = []

    import json

    try:
    #Opens and reads the JSON file into a list of User objects
        with open(file_name, mode='r') as jsonfile:
            json_data = json.load(jsonfile)
            user_data = [User.from_json(user) for user in json_data]

        while True:
        #Displays the menu options
            print("\nMenu options:\n 1: Age (min to max) \n 2: City \n 3: First Name \n 4: Last Name \n 5: ID (min to max)")
        
        #Asks the user to choose an option
            user_input = input("\nEnter a number to filter by or type 'Q' to quit: ").strip().upper()

        #Match statement to handle user's input
            match user_input:
                case "Q":
                    print("\nTerminating program. Goodbye!\n")
                    break
                case "1":
                    filtered_age = filter_by_age(user_data)
                    handle_filtered_data(filtered_age)
                case "2":
                    filtered_city = filter_by_city(user_data)
                    handle_filtered_data(filtered_city)
                case "3":
                    filtered_first_name = filter_by_first_name(user_data)
                    handle_filtered_data(filtered_first_name)
                case "4":
                    filtered_last_name = filter_by_last_name(user_data)
                    handle_filtered_data(filtered_last_name)
                case "5":
                    filtered_id = filter_by_id(user_data)
                    handle_filtered_data(filtered_id)
                case _:
                    #Prints if user enters an invalid option
                    print("\nInvalid input. Please enter a number between 1 and 5 or type 'Q' to quit.")
                    continue

        #Asks the user if they want to return to the main menu or quit
        while True:
            start_over = input("\nDo you want to return to the main menu? Y/N: ").strip().upper()
            if start_over == "Y":
                break
            elif start_over == "N":
                print("\nTerminating program. Goodbye!\n")
                exit()
            else:
                print("\nInvalid input. Please enter 'Y' or 'N'.")

    except FileNotFoundError:
    #Error displayed if main file is not found
        print(f"\nThe file {file_name} was not found.")

#Function to handle the filtered data: print it and give the user the option to save it to a new file/override existing file
def handle_filtered_data(filtered_data):
    if not filtered_data:
        print("\nNo results")
    else:
        #Prints the data in a pretty format in the terminal while maintaining the format from the original JSON file
        User.print_pretty(filtered_data)
        #Asks the user if they want to save the results into a new JSON file
        save_option = input("\nDo you want to save these results? Y/N: ").strip().upper()
        while save_option not in ["Y", "N"]:
            save_option = input("\nInvalid input. Please enter 'Y' or 'N': ").strip().upper()
        if save_option == "Y":
            while True:
                #Asks the user what they'd like to name their file with the results from their search
                filename = input("\nWhat should the name of the new file be? ").strip()
                #If the user does not enter a .json extension, this will auto add it for them
                if not filename.lower().endswith(".json"):
                    filename += ".json"
                    print(f"\nThe file name {filename} has been created.  Your data has been saved!")
                #If the file name already exists, this asks the user if they want to override the file
                if os.path.exists(filename):
                    overwrite = input(f"\nThe file '{filename}' already exists. Do you want to overwrite it? Y/N: ").strip().upper()
                    while overwrite not in ["Y", "N"]:
                        overwrite = input("\nInvalid input. Please enter 'Y' or 'N': ").strip().upper()
                    if overwrite == "Y":
                        break
                    else:
                        continue
                else:
                    break
            User.write_out_json(filtered_data, filename)

#Function to ask user to enter request for age or age range
def filter_by_age(user_data):
    while True:
        try:
            min_age = int(input("\nEnter minimum age: "))
            if min_age < 0:
                print("\nMinimum age cannot be less than 0. Please enter a valid minimum age.")
                continue
            break
        except ValueError:
            print("\nPlease enter a valid number for the minimum age.")

    while True:
        try:
            max_age = int(input("\nEnter maximum age: "))
            if min_age > max_age:
                print("\nMinimum age cannot be greater than maximum age.")
                continue
            break
        except ValueError:
            print("\nPlease enter a valid number for the maximum age.")

    #Gets/sets data from the user.py file
    if min_age == max_age:
        print(f"\nFiltered results for age = {min_age}:")
        filtered_data = [user for user in user_data if user.age_in_range(min_age, max_age)]
    else:
        print(f"\nFiltered results for age between {min_age} and {max_age}:")
        filtered_data = [user for user in user_data if user.age_in_range(min_age, max_age)]

    return filtered_data

#Function to filter data by city
def filter_by_city(user_data):
    while True:
        city = input("\nEnter the city to filter by: ").strip().title()
        if city:
            filtered_data = [user for user in user_data if user.get_city().title() == city]
            break
        else:
            print("\nCity cannot be empty. Please enter a valid city.")

    return filtered_data

#Function to filter data by first name
def filter_by_first_name(user_data):
    while True:
        first_name = input("\nEnter the first name to filter by: ").strip().title()
        if first_name:
            filtered_data = [user for user in user_data if user.get_first_name().title() == first_name]
            break
        else:
            print("\nFirst name cannot be empty. Please enter a valid first name.")

    return filtered_data

#Function to filter data by last name
def filter_by_last_name(user_data):
    while True:
        last_name = input("\nEnter the last name to filter by: ").strip().title()
        if last_name:
            filtered_data = [user for user in user_data if user.get_last_name().title() == last_name]
            break
        else:
            print("\nLast name cannot be empty. Please enter a valid last name.")

    return filtered_data

#Function to ask user to enter request for ID or ID range
def filter_by_id(user_data):
    while True:
        try:
            min_id = int(input("\nEnter minimum ID: "))
            if min_id < 0:
                print("\nMinimum ID cannot be less than 0. Please enter a valid minimum ID.")
                continue
            break
        except ValueError:
            print("\nPlease enter a valid number for the minimum ID.")

    while True:
        try:
            max_id = int(input("\nEnter maximum ID: "))
            if min_id > max_id:
                print("\nMinimum ID cannot be greater than maximum ID.")
                continue
            break
        except ValueError:
            print("\nPlease enter a valid number for the maximum ID.")

    #Gets/sets data from the user.py file
    if min_id == max_id:
        print(f"\nFiltered results for ID = {min_id}: ")
        filtered_data = [user for user in user_data if user.id_in_range(min_id, max_id)]
    else:
        print(f"\nFiltered results for IDs between {min_id} and {max_id}:")
        filtered_data = [user for user in user_data if user.id_in_range(min_id, max_id)]

    #Returns the data
    return filtered_data

#Calls the main function
if __name__ == "__main__":
    main()