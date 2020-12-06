
from entity.Task import Task
from intrefaces.TaskRepository import TaskRepository
from xml.dom import minidom

class TaskRepositoryXML(TaskRepository):
    def __init__(self):
        self.myFile = minidom.parse('1.xml')

    def show_all(self) -> Union[List[Task], str]:
        items = mydoc.getElementsByTagName('item')
