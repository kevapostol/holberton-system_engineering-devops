#!/usr/bin/python3
"""
This module exports a CSV file
"""

import requests
from sys import argv

if __name__ == "__main__":
    uri = "https://jsonplaceholder.typicode.com"

    response = requests.get(uri + "/users/{}".format(argv[1]))
    obj = response.json()
    username = obj.get("username")
    response = requests.get(uri + "/todos?userId={}".format(argv[1]))
    obj_list = response.json()

    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        for task in obj_list:
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                          task.get("userId"),
                          username,
                          task.get("completed"),
                          task.get("title")))
