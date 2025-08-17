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
    remove_parser = sub_parser.add_parser("delete",help="Remove task of given Id")
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

#create task item and return it
def create_task(id, task):
    item = {}
    item['id'] = id + 1
    item['task'] = task
    item['status'] = 'todo'
    item['created_at'] = datetime.now().isoformat()
    item['updated_at'] = datetime.now().isoformat()
    print(item)
    return item

#add task method
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

#update task method
def update_task(task_id, task):
    with open(FILE_NAME,'r') as f:
        data = json.load(f)
    
    #in-place mutate
    '''for item in data:
        if item['id'] == id:
            item['task'] = task
    '''
    #More pythonic way list comprehensions
    data = [
        {**item, 'task': task} if item['id'] == int(task_id) else item
        for item in data
    ]    
    with open(FILE_NAME,'w') as f:
        json.dump(data,f,indent=4)   

def remove_task(task_id):
    with open(FILE_NAME,'r') as f:
        data = json.load(f)
    
    '''data = [
        item if item['id'] != int(task_id)
        for item in data
    ]'''

    data = [item for item in data if item['id'] != int(task_id)]

    data = list(filter(
        lambda item: item['id'] != int(task_id),
        data
    ))
    
    with open(FILE_NAME,'w') as f:
        json.dump(data,f,indent=4)  


if __name__ == '__main__':
    parser = command_line_setup()
    args = parser.parse_args()
    if args.command == 'add':
        add_task(args)
    elif args.command == 'update':
        update_task(args.id, args.task)
    elif args.command == 'delete':
        remove_task(args.id)
