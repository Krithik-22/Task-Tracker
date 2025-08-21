from task_manager import TaskManager
from cli_commands import command_line_setup

if __name__ == '__main__':
    task_manager = TaskManager()

    COMMANDS = {
        "add": lambda args : task_manager.add_task(args.task),
        "delete": lambda args : task_manager.remove_task(args.id),
        "update": lambda args : task_manager.get_task(args.id).update_task(args.task),
        "mark-in-progress": lambda args : task_manager.get_task(args.id).mark_in_progress(),
        "mark-done": lambda args : task_manager.get_task(args.id).mark_done(),
        "list": lambda args : task_manager.list_all_tasks(getattr(args,'filter'))
    }

    parser = command_line_setup()
    args = parser.parse_args()

    if args.command:
        COMMANDS[args.command](args)
    else:
        parser.print_help