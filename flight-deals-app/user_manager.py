import requests
from dotenv import load_dotenv
import os

load_dotenv()

users_endpoint = os.environ["USER_ENDPOINT"]


class UserManager:
    def create_user(self):

        print(
            "Welcome to Felipe's Flight CLub.\nWe find the best flight    deals  and email you."
        )
        first_name = input("What is your first name? ")
        last_name = input("What is your last name? ")
        email = input("What is your email? ")
        checked_email = input("Type your email again. ")

        if email == checked_email:

            user_input = {
                "user": {"firstName": first_name, "lastName": last_name, "email": email}
            }
            response = requests.post(url=users_endpoint, json=user_input)
            print(response.text)
            print("You're in the club!")
