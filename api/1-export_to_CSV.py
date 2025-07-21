#!/usr/bin/python3
"""
Exports all tasks for a given employee ID to a CSV file.
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""

import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    # Get user information
    user_response = requests.get("{}/users/{}".format(url, employee_id))
    user_data = user_response.json()
    employee_name = user_data.get("name")
    username = user_data.get("username")

    # Get TODO list for the employee
    todos_response = requests.get("{}/todos?userId={}".format(
        url, employee_id))
    todos = todos_response.json()

    # Count completed tasks
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    number_of_done_tasks = len(done_tasks)

    # Print results to console
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))

    # Export to CSV
    filename = "{}.csv".format(employee_id)
    with open(filename, mode="w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])
