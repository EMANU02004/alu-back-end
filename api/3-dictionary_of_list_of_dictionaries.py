
#!/usr/bin/python3
"""
Exports all employees' TODO lists to JSON format.
"""
import json
import requests


if __name__ == "__main__":
    # Get all users
    users_response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )
    users = users_response.json()

    # Get all todos
    todos_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    )
    todos = todos_response.json()

    all_data = {}

    # Organize tasks by user
    for user in users:
        user_id = str(user.get("id"))  # MUST be string
        username = user.get("username")

        user_tasks = []

        for task in todos:
            if task.get("userId") == user.get("id"):
                task_dict = {
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                user_tasks.append(task_dict)

        all_data[user_id] = user_tasks

    # Write to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file)
