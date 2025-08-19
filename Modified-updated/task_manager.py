from dataclasses import asdict
import os
import json
from datetime import datetime
from tasks import Task

class taskManager:
    def __init__(self, file_name='tasks.json'):
        self.file_name = file_name
        self.tasks = self.load_data()

    def load_data(self):
        if not os.path.exists(self.file_name):
            return []
        try:
            with open(self.file_name,'r') as f:
                data = [Task(**t) for t in json.load(f)]
        except json.JSONDecodeError:
            data = []
        return data
    
    def save_data(self):
        with open(self.file_name,'w') as f:
            data = [asdict(t) for t in self.tasks]
            json.dump(data,f,indent=4)

    def add_task(self,task_desc):
        id = max([t.id for t in self.tasks], default=0) + 1
        task = Task(id,task_desc)
        self.tasks.append(task)
        self.save_data()
        print(f'Task added successfully: ID({id})')

    def remove_task(self,task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_data()

    def list_all_tasks(self,filter='all'):
        if filter == 'in-progress':
            print([asdict(t) for t in self.tasks if t.status == 'in-progress'])
        elif filter == 'done':
            print([asdict(t) for t in self.tasks if t.status == 'done'])
        else:
            print([asdict(t) for t in self.tasks])