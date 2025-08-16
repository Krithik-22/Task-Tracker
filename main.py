import argparse
import os
import json
from datetime import datetime


id_cnt = 1
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

def create_task(task):
    global id_cnt
    item = {}
    item['id'] = id_cnt
    id_cnt += 1
    item['task'] = task
    item['status'] = 'todo'
    item['created_at'] = datetime.now().isoformat()
    item['updated_at'] = datetime.now().isoformat()
    return item

def add_task(args):
    item = create_task(args.task)
    with open(FILE_NAME,'w+') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
        data.append(item)
        json.dump(data,f)

if __name__ == '__main__':
    parser = command_line_setup()
    args = parser.parse_args()
    if args.command == 'add':
        add_task(args)
