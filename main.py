import argparse
import os
import json
from datetime import datetime

FILE_NAME = 'tasks.json'

def command_line_setup():
    parser = argparse.ArgumentParser(prog="Task CLI")
    sub_parser = parser.add_subparsers(dest="command")

    #add command
    add_parser = sub_parser.add_parser("add",help="Add a new task")
    add_parser.add_argument("task",help="Task to add")

    #update command
    update_parser = sub_parser.add_parser("update",help="Update task of given Id")
    update_parser.add_argument("id",help="Which task Id to Update")
    update_parser.add_argument("task",help="Updated new task")

    #remove command
    remove_parser = sub_parser.add_parser("remove",help="Remove task of given Id")
    remove_parser.add_argument("id",help="Which task Id to Remove")

    return parser



def create_file():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,'w') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    return data

def create_task(id, task):
    item = {}
    item['id'] = id + 1
    item['task'] = task
    item['status'] = 'todo'
    item['created_at'] = datetime.now().isoformat()
    item['updated_at'] = datetime.now().isoformat()
    print(item)
    return item

def add_task(args):
    data = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    item = create_task(len(data),args.task)
    data.append(item)
    with open(FILE_NAME,'w') as f:
        json.dump(data,f,indent=4)

if __name__ == '__main__':
    parser = command_line_setup()
    args = parser.parse_args()
    if args.command == 'add':
        add_task(args)
