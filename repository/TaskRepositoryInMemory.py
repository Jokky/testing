from typing import List, Union
import datetime

from entity.Task import Task
from intrefaces.TaskRepository import TaskRepository


class TaskRepositoryInMemory(TaskRepository):
    def __init__(self):
        self.__tasks = [Task(1, 'Задача 1', 'Описание задачи', '2020-12-01', None)]

    def show_all(self) -> Union[List[Task], str]:
        return self.__tasks

    def show(self, task_id: int) -> Union[Task, str]:
        for task in self.__tasks:
            if task_id == task.id:
                return task.to_string() + '\n'
        return 'Не найдена задача'

    def add(self, task: Task) -> bool:
        max_id = 0
        for i in self.__tasks:
            if i.id > max_id:
                max_id = i.id
        max_id += 1
        now = datetime.datetime.now()
        create_at = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

        task.id = max_id
        task.create_at = str(create_at)
        task.update_at = None
        self.__tasks.append(task)

        return True

    def delete(self, task_id: int) -> bool:
        pos = -1
        for i in range(len(self.__tasks)):
            task = self.__tasks[i]

            if task.id == id:
                pos = i
                break

        if pos > -1:
            del self.__tasks[pos]
            return True

        return False

    def update(self, task: Task) -> bool:
        max_id = 0
        for i in self.__tasks:
            if i.id > max_id:
                max_id = i.id
        max_id += 1
        now = datetime.datetime.now()
        create_at = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

        task.id = max_id
        task.create_at = str(create_at)
        task.update_at = None
        self.__tasks.append(task)

        return True
