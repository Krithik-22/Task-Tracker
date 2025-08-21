from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Task:
    id: int
    task: str
    status: str = 'todo'
    created_at: str = datetime.now().isoformat()
    updated_at: str = datetime.now().isoformat()

    def mark_done(self):
        self.status = 'done'
        self.updated_at = datetime.now().isoformat()
    
    def mark_in_progress(self):
        print(self.status)
        self.status = 'in-progress'
        print(self.status)
        self.updated_at = datetime.now().isoformat()

    def update_task(self,new_task):
        self.task = new_task
        self.updated_at = datetime.now().isoformat()