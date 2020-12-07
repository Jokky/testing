
from entity.Task import Task
from repository.TaskRepositoryInXML import TaskRepositoryXML

tasks_repository = TaskRepositoryXML()


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
            tasks = tasks_repository.show_all()
            result = ''
            for task in tasks:
                result += task.to_string() + '\n'
            print(result)
        if command_num == 2:
            task_id = int(input('Номер задачи: '))
            result = tasks_repository.show(task_id)
            if isinstance(result, Task):
                print(result.to_string())
            else:
                print(result)
        if command_num == 3:
            task = Task()
            task.title = input('Введите заголовок: ')
            task.description = input('Введите описание: ')

            result = tasks_repository.add(task)

            if result:
                print('Задача добавлена')
        if command_num == 4:
            remove_1 = int(input('номер задачи для удаления: '))
            tasks_repository.delete(remove_1)
        if command_num == 5:
            task = Task()
            task.id = int(input('введите номер задачи для изменения: '))
            task.title = input('заголовок задачи: ')
            task.description = input('описание задачи: ')

            tasks_repository.update(task)

    return False


if __name__ == '__main__':
    run()
