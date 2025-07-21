#!/usr/bin/python3
"""
This script retrieves TODO list progress for a given employee ID
from the JSONPlaceholder API and exports the data to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"

    # Get user information
    user_response = requests.get(f"{url}/users/{employee_id}")
    user_data = user_response.json()
    username = user_data.get("username")

    # Get TODO list for the employee
    todos_response = requests.get(f"{url}/todos?userId={employee_id}")
    todos = todos_response.json()

    # Format the data
    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    result = {employee_id: tasks}

    # Export to JSON file
    with open(f"{employee_id}.json", "w", encoding='utf-8') as jsonfile:
        json.dump(result, jsonfile)
