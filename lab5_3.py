# =============================================================================
# Student Name: Doniel O'Niel
# Lab Title: Lab 5 
# Date: May 28, 2026
# =============================================================================
# Task 1
from pathlib import Path
import json


def store_task_list(task_list):
    '''Saves the task list to a JSON file called task_list.json.'''
    file_path = Path("task_list.json")
    json_string = json.dumps(task_list)
    file_path.write_text(json_string)
    print("Task list saved successfully.")


def load_task_list():
    '''Loads the task list from task_list.json.
    Returns the list if the file exists, otherwise returns an empty list.
    '''
    file_path = Path("task_list.json")
    if file_path.exists():
        contents = file_path.read_text()
        return json.loads(contents)
    return []
