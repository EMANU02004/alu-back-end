#!/usr/bin/python3

import sys
import requests

def fetch_employee(employee_id: int):
    # Get employee information
    user_resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user_resp.raise_for_status()
    user = user_resp.json()
    # Get todos for the employee
    todos_resp = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos_resp.raise_for_status()
    todos = todos_resp.json()
    return user, todos

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 0-gather_data_from_an_API.py <employee_id>')
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('Employee ID must be an integer')
        sys.exit(1)

    user, todos = fetch_employee(employee_id)
    total_tasks = len(todos)
    done_tasks = [t for t in todos if t.get('completed')]
    num_done = len(done_tasks)
    print(f"Employee {user.get('name')} is done with tasks({num_done}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == '__main__':
    main()

