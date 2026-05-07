#!/usr/bin/python3
"""
Python script that returns information about an employee's TODO list progress
using a REST API.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        base_url = "https://jsonplaceholder.typicode.com/"
        
        # Get user info
        user_res = requests.get("{}users/{}".format(base_url, emp_id))
        user_data = user_res.json()
        
        # Get todo info
        todo_res = requests.get("{}todos?userId={}".format(base_url, emp_id))
        todo_data = todo_res.json()
        
        # Task 0 uses 'name'
        emp_name = user_data.get("name")
        all_tasks = todo_data
        done_tasks = [t for t in all_tasks if t.get("completed") is True]
        
        print("Employee {} is done with tasks({}/{}):".format(
            emp_name, len(done_tasks), len(all_tasks)))
        
        for task in done_tasks:
            # Format: 1 tabulation and 1 space
            print("\t {}".format(task.get("title")))
