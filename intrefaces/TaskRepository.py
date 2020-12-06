from typing import List, Union

from entity.Task import Task


class TaskRepository:
    # Получить задачу по id
    def show(self, task_id: int) -> Union[Task, str]:
        pass

    # Показать все задачи
    def show_all(self) -> Union[List[Task], str]:
        pass

    # Добавить задачу
    def add(self, task: Task) -> bool:
        pass

    # Обноыить задачу
    def update(self, task: Task) -> bool:
        pass

    # Удалить задачу по id
    def delete(self, task_id: int) -> bool:
        pass
