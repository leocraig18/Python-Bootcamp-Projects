import requests
import os

sheety_users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")


def add_user(parameters):
    response = requests.post(url=sheety_users_endpoint, json=parameters)
    return response


# User Prompts
print("Welcome to Eclipse Flight Club\nWhere we find the best flight deals and email them to you!")
first_name = (input("\nWhat is your first name?\n")).title()
last_name = (input("\nWhat is your surname?\n")).title()
email = input("\nWhat is your email?\n")
repeat_email = input("\nConfirm email:\n")


if email == repeat_email:
    print("Thank you for signing up\nWelcome to the Club!")
    data = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }
    response = add_user(data)
    print("response.status_code =", response.status_code)
    print("response.text =", response.text)
else:
    print("Sorry your emails didn't match. Please retry.")
