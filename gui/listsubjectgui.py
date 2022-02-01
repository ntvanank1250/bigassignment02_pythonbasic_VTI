from bll import SubjectBLL
from dto import SubjectDto
from tabulate import tabulate

class ListSubjectGUI:
    def __init__(self):
        self.__sjBLL = SubjectBLL()

    def openScreen(self):
        print('*** List of Subjects ***')
        result = self.__sjBLL.getAll()
    
        print(tabulate(result, headers=('SubjectCode','Subjectname')))
      
