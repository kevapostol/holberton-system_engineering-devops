#!/usr/bin/python3
"""
This module exports a JSON file
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    # Endpoint
    uri = "https://jsonplaceholder.typicode.com"

    # Making a GET request for 'USER'
    response = requests.get(uri + "/users/{}".format(argv[1]))
    obj = response.json()
    name = obj.get("name")
    response = requests.get(uri + "/todos?userId={}".format(argv[1]))
    obj_list = response.json()

    user_tasks = []

    for ea_task in obj_list:
        user_tasks.append({
                          "task": ea_task.get("title"),
                          "completed": ea_task.get("completed"),
                          "username": name
                          })

    user_dict = {argv[1]: user_tasks}
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as json_file:
        json.dump(user_dict, json_file)
