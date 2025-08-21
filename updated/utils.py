from dataclasses import dataclass, asdict
from datetime import datetime
import argparse
import os
import json

FILE_NAME = 'tasks.json'

@dataclass
class Task:
    id
    task
    status = 'todo'
    created_at = datetime.now().isoformat()
    updated_at = datetime.now().isoformat()

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    return data

