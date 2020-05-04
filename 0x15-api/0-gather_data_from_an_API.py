#!/usr/bin/python3
"""
This module gathers data from an API
"""

import requests
from sys import argv

if __name__ == "__main__":
    # Endpoint
    uri = "https://jsonplaceholder.typicode.com"

    # Making a GET request for 'USER'
    response = requests.get(uri + "/users/{}".format(argv[1]))

    # # HTTP Response code
    # print("Response: " + str(response))

    obj = response.json()
    name = obj.get("name")

    # Making a GET request to TODOS by USER_ID
    response = requests.get(uri + "/todos?userId={}".format(argv[1]))
    obj_list = response.json()
    complete = 0
    num_tasks = len(obj_list)

    # Counts the completed tasks
    for ea_todo in obj_list:
        if ea_todo.get("completed") is True:
            complete += 1

    print("Employee {} is done with tasks ({}/{}):".format(name, complete,
          num_tasks))

    # Prints the completed tasks
    for ea_todo in obj_list:
        if ea_todo.get("completed") is True:
            print("\t {}".format(ea_todo.get("title")))
