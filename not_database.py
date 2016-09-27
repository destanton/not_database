import csv
import sys

with open("stored_info.csv", newline="") as csvfile:
    reader = list(csv.DictReader(csvfile))
    print(list(reader)[0]["full_name"])


def login(reader):
        username = input("What's your Username? ")
        password = input("What's your Password? ")
        for line in reader:
            if username == line["username"] and password == line["password"]:
                print(username, password)
                create_user(reader)
                
        # for line in reader:
        #     if password in line["password"]:
        #         return password
        #     print(password)
            # print(line["username"])
            # if username ==:
            #     print(





def create_user(reader):
    input("Would you like to [C]reate a new user or [L]og out? \n>").lower()
    if input != "l":
        full_name = input("Enter your full name:\n> ")
        username = input("Pick a username:\n> ")
        password = input("Enter your password:\n> ")
        random_fact = input("What's a random fact about yourself?\n> ")
    else:
        print("Have a good day!")
        sys.exit()

    with open("stored_info.csv", "a") as csvfile:
        fieldnames = ["full_name", "user_name", "password", "random_fact"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"full_name": "{}".format(full_name), "user_name": "{}".format(username), "password": "{}".format(password), "random_fact": "{}".format(random_fact)})
#
login(reader)
# # print(stored_info.writerow)
