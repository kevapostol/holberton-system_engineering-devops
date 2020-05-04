#!/usr/bin/python3
"""
This module gathers data from an API
"""

import requests
from sys import argv

if __name__ == "__main__":
    uri = "https://jsonplaceholder.typicode.com"

    response = requests.get(uri + "/users/{}".format(argv[1]))
    obj = response.json()
    name = obj.get("name")

    response = requests.get(uri + "/todos?userId={}".format(argv[1]))
    obj_list = response.json()
    num_tasks = len(obj_list)

    completed_task = []
    for ea_todo in obj_list:
            if ea_todo.get("completed") is True:
                completed_task.append(ea_todo)

    completed_tasks = len(completed_task)
    print("Employee {} is done with tasks ({}/{}):".format(name,
          completed_tasks, num_tasks))

    # Prints the completed tasks
    for ea_todo in completed_task:
            print("\t {}".format(ea_todo.get("title")))
