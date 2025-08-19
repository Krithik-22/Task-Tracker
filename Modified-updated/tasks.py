from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Task:
    id
    task
    status = 'todo'
    created_at = datetime.now().isoformat()
    updated_at = datetime.now().isoformat()

    def mark_done(self):
        self.status = 'done'
        self.updated_at = datetime.now().isoformat()
    
    def mark_in_progress(self):
        self.status = 'in-progress'
        self.updated_at = datetime.now().isoformat()

    def update_task(self,new_task):
        self.task = new_task
        self.updated_at = datetime.now().isoformat()