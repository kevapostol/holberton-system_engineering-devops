#!/usr/bin/python3
"""
This module exports a CSV file
"""

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

    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        for task in obj_list:
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                          task.get("userId"),
                          name,
                          task.get("completed"),
                          task.get("title")))
