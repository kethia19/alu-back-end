#!/usr/bin/python3
"""
This script retrieves TODO tasks for all employees
from the JSONPlaceholder API and exports the data to a JSON file.

Format:
{
  "USER_ID": [
    {
      "username": "USERNAME",
      "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS
    },
    ...
  ],
  ...
}
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    # Get all users
    users_response = requests.get(f"{url}/users")
    users = users_response.json()

    all_tasks = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        # Get the user's todos
        todos_response = requests.get(f"{url}/todos?userId={user_id}")
        todos = todos_response.json()

        task_list = []
        for task in todos:
            task_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        all_tasks[user_id] = task_list

    # Write to file
    with open("todo_all_employees.json", "w", encoding='utf-8') as jsonfile:
        json.dump(all_tasks, jsonfile)
