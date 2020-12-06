from datetime import datetime
from typing import Union, List

import pymysql
from pymysql.cursors import DictCursor

from entity.Task import Task
from intrefaces.TaskRepository import TaskRepository


def task(args):
    pass


class TaskRepositoryMySQL(TaskRepository):
    def __init__(self):
        self.driver = pymysql.connect(
            host='37.140.192.195',
            user='u1199897_task_ad',
            password='0X3c9P3g',
            db='u1199897_task',
            cursorclass=DictCursor
        )

    def show_all(self) -> Union[List[Task], str]:
        cursor = self.driver.cursor()

        with cursor:
            cursor.execute('SELECT * FROM task')
            result = cursor.fetchall()
            tasks = []
            for i in range(len(result)):
                t = result[i]
                n = Task(
                    id=t.get('task_id'),
                    title=t.get('title'),
                    description=t.get('description'),
                    create_at=t.get('create_at'),
                    update_at=t.get('update_at')
                )
                tasks.append(n)

            return tasks

        return 'Нет задач'

    def show(self, task_id: int) -> Union[Task, str]:
        cursor = self.driver.cursor()
        with cursor:
            cursor.execute('SELECT * FROM task WHERE task_id = ' + str(task_id))
            rows = cursor.fetchall()
            for row in rows:
                return Task(
                    id=row.get('task_id'),
                    title=row.get('title'),
                    description=row.get('description'),
                    create_at=row.get('create_at'),
                    update_at=row.get('update_at')
                )

            return 'ne naydeno'

    def add(self, task: Task) -> bool:
        cursor = self.driver.cursor()
        now = datetime.now()
        date = '{}-{}-{}'.format(now.year, now.month, now.day)
        with cursor:
            sql = "INSERT INTO task (title, description, create_at) VALUES ('{}', '{}', '{}')".format(task.title,
                                                                                                      task.description,
                                                                                                      date)
            cursor.execute(sql)
            self.driver.commit()

            return True

    def update(self, task: Task) -> bool:
        cursor = self.driver.cursor()
        with cursor:
            # rows = cursor.fetchall()

            sql = "UPDATE task SET title = '{}', description = '{}' WHERE task_id = '{}'".format(task.title, task.description, str(task.id))
            cursor.execute(sql)

        return True

    def delete(self, task_id: int) -> bool:
        cursor = self.driver.cursor()
        with cursor:
            sql = ("DELETE FROM task WHERE task_id =" + (str(task_id)))
            cursor.execute(sql)

        return True
