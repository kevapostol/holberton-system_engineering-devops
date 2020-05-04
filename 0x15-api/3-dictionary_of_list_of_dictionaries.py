#!/usr/bin/python3
"""
This module exports a JSON file
"""

import json
import requests
from sys import argv


def get_username(uri):
    """
    Gets the name of the user
    """
    response = requests.get(uri)
    obj = response.json()
    return obj.get("username")


def get_tasks(uri, username):
    """
    Sets a list for the user
    """
    response = requests.get(uri)
    obj_list = response.json()
    user_tasks = []

    for ea_task in obj_list:
        user_tasks.append({
                          "username": username,
                          "task": ea_task.get("title"),
                          "completed": ea_task.get("completed")
                          })

    return user_tasks

if __name__ == "__main__":
    uri = "https://jsonplaceholder.typicode.com"

    response = requests.get(uri + "/users")
    obj_users = response.json()
    dicts = {}

    for ea_user in obj_users:
        dicts[str(ea_user.get("id"))] = []

    for key in dicts:
        username = get_username(uri + "/users/{}".format(key))
        task_list = get_tasks(uri + "/todos?userId={}".format(key), username)
        dicts[key] = task_list

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(dicts, json_file)
