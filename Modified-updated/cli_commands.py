import argparse

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

    status_progress_parser = sub_parser.add_parser("mark-in-progress", help="Update the status of task to in-progress")
    status_progress_parser.add_argument("id",help="Which task Id to update status")

    status_done_parser = sub_parser.add_parser("mark-done", help="Update the status of task to done")
    status_done_parser.add_argument("id",help="Which task Id to update status")

    list_parser = sub_parser.add_parser("list",help="List the tasks")
    list_parser.add_argument("filter",nargs='?',default='all',help="Status filter")

    return parser