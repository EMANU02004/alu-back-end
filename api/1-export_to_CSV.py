#!/usr/bin/python3
"""Script to export an employee's TODO list to CSV format."""

import csv
import requests
import sys


def main():
    """Fetch an employee's tasks and write them to USER_ID.csv."""
    user_id = int(sys.argv[1])
    base = 'https://jsonplaceholder.typicode.com'

    user = requests.get('{}/users/{}'.format(base, user_id)).json()
    username = user.get('username')

    todos = requests.get('{}/todos'.format(base),
                         params={'userId': user_id}).json()

    filename = '{}.csv'.format(user_id)
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username,
                             task.get('completed'), task.get('title')])


if __name__ == '__main__':
    main()       
