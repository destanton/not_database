import csv
import sys


    # print((reader)[0]["full_name"])


def login():
    username = input("What's your Username? ").lower()
    password = input("What's your Password? ").lower()
    with open("stored_info.csv") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=["full_name", "username", "password", "extra information"])

        for row in reader:
            # print(row["username"])
            # print(row["password"])
            if username == row["username"].lower():
                if password == row["password"].lower():
                    # print(username, password)
                    logged_in()
        else:  # username != line["username"] or password != line["password"]:
            print("Invalid entry, please try again")
            login()
    # for line in reader:
    #     if password in line["password"]:
    #         return password
    #     print(password)
        # print(line["username"])
        # if username ==:
        #     print(


def logged_in():
    choice = input("Would you like to [C]reate a new user or [L]og out? ").lower()
    if choice == "l":
        print("Have a good day!")
        sys.exit()

    elif choice == "c":
        user_validation()
    else:
        print("Invalid entry")
        logged_in()


def create_user():
    pass
    # full_name = input("Enter your full name:\n> ")
    # password = input("Enter your password:\n> ")
    # random_fact = input("What's a random fact about yourself?\n> ")
    #
    # with open("stored_info.csv", "a") as csvfile:
    #     fieldnames = ["full_name", "user_name", "password", "random_fact"]
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     writer.writerow({"full_name": "{}".format(full_name), "user_name": "{}".format(username), "password": "{}".format(password), "random_fact": "{}".format(random_fact)})


def user_validation():
    username = input("Pick a username:\n> ")
    with open("stored_info.csv") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=["full_name", "username", "password", "extra information"])
        # print(list(reader))
        for row in reader:
            # print(row["username"])
            if username.lower() == row["username"].lower():
                print("That username is not available")
                user_validation()
        else:
            print("Success! That name is available")

    full_name = input("Enter your full name:\n> ")
    password = input("Enter your password:\n> ")
    random_fact = input("What's a random fact about yourself?\n> ")

    with open("stored_info.csv", "a") as csvfile:
        fieldnames = ["full_name", "user_name", "password", "random_fact"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"full_name": "{}".format(full_name), "user_name": "{}".format(username), "password": "{}".format(password), "random_fact": "{}".format(random_fact)})
    logged_in()
#
login()
# # print(stored_info.writerow)
