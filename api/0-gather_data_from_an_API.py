#!/usr/bin/python3
"""Gather data from an API"""
import json
import sys
from urllib.request import urlopen


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_id
    )

    with urlopen(user_url) as response:
        user = json.loads(response.read().decode("utf-8"))

    with urlopen(todos_url) as response:
        todos = json.loads(response.read().decode("utf-8"))

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), len(todos)
    ))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
