tasks = [{'title': 'Задача 1', 'description': 'Описание задачи', 'create_at': '2020-12-01', 'update_at': None}]


def show_all_tasks() -> str:
    if len(tasks) == 0:
        return 'Нет задач'

    result = ''

    for task in tasks:
        result += 'Задача №' + task.id + '. Заголовок: ' + task.title + '. Описание: ' + task.description + '\n'

    return result


# Найти задачу и отобразить по шаблону
def show_task(id: int) -> str:
    return ''


# Найти задачу в списке и заменить на отредактированную
def edit_task(task: dict) -> bool:
    return False


# Добавить задачу в конец списка
def add_task(task: dict) -> bool:
    return False


# Удалить задачу в массиве по id задачи
def remove_task(id: int) -> bool:
    return False


# Написать логику управления с консоли
# 1) Идет выбор команды:
#    1. Показать все задачи
#    2. Показать задачу
#    3. Добавить здаачу
#    4. Удалить задачу
#
# 2) После выбора команды необходимо очистить консоль и отобразить необходимую подсказку для куоманды. Например,
# для удаления неоюходимо сообщать выводить следующее сообщение "Введите id задачи"
def run():
    return False


if __name__ == '__main__':
    run()
