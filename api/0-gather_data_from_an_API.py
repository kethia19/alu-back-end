#!/usr/bin/python3
"""
This script retrieves TODO list progress for a given employee ID
from the JSONPlaceholder API and displays the progress in a
specified format.
"""

import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    # Get user information
    user_response = requests.get("{}/users/{}".format(url, employee_id))
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get TODO list for the employee
    todos_response = requests.get("{}/todos?userId={}".format(
        url, employee_id))
    todos = todos_response.json()

    # Count completed tasks
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    number_of_done_tasks = len(done_tasks)

    # Print results
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
