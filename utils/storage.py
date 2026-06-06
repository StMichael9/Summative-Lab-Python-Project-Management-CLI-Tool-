import json
import os

from models.user import User

filename = "db.json"

def save_data(data):
    # Converting list of User objects into dictionaries using a list comprehension
    raw_users = [user.to_dict() for user in data]

    with open (filename, "w") as file:
        json.dump(raw_users, file, indent=4)

def load_data():
    # Check if the file DOES NOT exist on the system yet
    if not os.path.exists(filename):
        return []
    
    # If it does exist, open it in read mode
    with open (filename, "r") as file:
        raw_data = json.load(file)

    return [User.from_dict(user_dict) for user_dict in raw_data]