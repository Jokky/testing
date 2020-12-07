import os
from typing import Union, List
from entity.Task import Task
from intrefaces.TaskRepository import TaskRepository
import xml.etree.cElementTree as ET

XML_FILE = os.path.join(os.environ['HOME'], '/Users/dmitryyakushev/PycharmProjects/tasking/repository/1.xml')


class TaskRepositoryXML(TaskRepository):
    def __init__(self):
        myFiletre = ET.ElementTree(file=XML_FILE)
        self.root = myFiletre.getroot()

    def show_all(self) -> Union[List[Task], str]:
        tasks = []
        for elem in self.root:
            task = {}
            for child in elem:
                task[child.tag] = child.text

            tasks.append(Task(
                id=int(task.get('id')),
                title=task.get('title'),
                description=task.get('description'),
                create_at=task.get('create'),
                update_at=task.get('update'),
            ))

        return tasks
