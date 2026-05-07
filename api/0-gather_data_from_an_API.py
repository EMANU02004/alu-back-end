#!/usr/bin/python3
"""Fetches employee TODO list progress from REST API"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    BASE_URL = "https://jsonplaceholder.typicode.com/"
    user_url = "{}/users/{}".format(BASE_URL, employee_id)
    todos_url = "{}/todos?userId={}".format(BASE_URL, employee_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), len(todos)
    ))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
