import datetime
tasks = [{'id': 1, 'title': 'Задача 1', 'description': 'Описание задачи', 'create_at': '2020-12-01', 'update_at': None}]


def show_all_tasks() -> str:
    if len(tasks) == 0:
        return 'Нет задач'

    result = ''

    for task in tasks:
        result += 'Задача №' + str(task.get('id')) + '. Заголовок: ' + task.get('title') + '. Описание: ' + task.get(
            'description') + '\n'

    return result


# Найти задачу и отобразить по шаблону
def show_task(id: int) -> str:
    for task in tasks:
        if id == task.get('id'):
            return 'Задача №' + str(task.get('id')) + '. Заголовок: ' + task.get('title') + '. Описание: ' + task.get(
                'description') + '\n'
    return 'Не найдена задача'


# Найти задачу в списке и заменить на отредактированную
def edit_task(task: dict) -> bool:
    pos = -1
    for i in range(len(tasks)):
        t = tasks[i]
        if t.get('id') == task.get('id'):
            pos = i
            break

    if pos == -1:
        return False

    tasks[pos]['title'] = task.get('title')
    tasks[pos]['description'] = task.get('description')

    return True


# Добавить задачу в конец списка
def add_task(task: dict) -> bool:
    max_id = 0
    for i in tasks:
        if i.get('id') > max_id:
            max_id = i.get('id')
    max_id += 1
    now = datetime.datetime.now()
    create_at = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

    task['id'] = max_id
    task['create_at'] = str(create_at)
    task['update_at'] = None
    tasks.append(task)

    return True


# Удалить задачу в массиве по id задачи
def remove_task(id: int) -> bool:
    pos = -1
    for i in range(len(tasks)):
        task = tasks[i]

        if task.get('id') == id:
            pos = i
            break

    if pos > -1:
        del tasks[pos]
        return True

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
    # print(show_all_tasks())
    # print(show_task(1))
    # print(remove_task(1))
    # print(add_task({'title': 'Добавленная задача', 'description': 'Описание новой задачи'}))
    # print(edit_task({'id': 2, 'title': 'Новый заголовок у задачи', 'description': 'Новое описание'}))

    while True:
        print('Введите номер команды:')
        print('1. Показать все задачи\n2. Показать задачу\n3. Добавить задачу\n4. Удалить задачу\n5. Изменить задача')

        command_num = int(input('Номер команды: '))
        if command_num == -1:
            break

        if command_num == 1:
            print(show_all_tasks())
        if command_num == 2:
            task_id = int(input('Номер задачи: '))
            print(show_task(task_id))
        if command_num == 3:
            task = {}
            task['title'] = input('Введите заголовок: ')
            task['description'] = input('Введите заголовок: ')

            result = add_task(task)

            if result:
                print('Задача добавлена')
        if command_num == 4:
            remove_1 = int(input('номер задачи для удаления: '))
            remove_task(remove_1)
        if command_num == 5:
            task = {}
            task['id'] = int(input('введите номер задачи для изменения: '))
            task['title'] = input('заголовок задачи: ')
            task['description'] = input('описание задачи: ')

            edit_task(task)

    return False


if __name__ == '__main__':
    run()
