from typing import Union


class Task:
    def __init__(self, id: int = -1, title: str = '', description: str = '', create_at: str = '', update_at: Union[str, None] = None):
        self.id = id
        self.title = title
        self.description = description
        self.create_at = create_at
        self.update_at = update_at

    def to_string(self):
        return 'Задача №' + str(self.id) + '. Заголовок: ' + self.title + '. Описание: ' + self.description
