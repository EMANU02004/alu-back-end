#!/usr/bin/python3
"""For a given employee ID, returns information about TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/" + str(employee_id)).json()
    todos = requests.get(
        url + "/todos", params={"userId": employee_id}).json()
    name = user.get("name")
    done = [t for t in todos if t.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done), len(todos)))
    for task in done:
        print("\t " + task.get("title"))

