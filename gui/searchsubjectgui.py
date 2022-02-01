from bll import SubjectBLL
from dto import SubjectDto
from tabulate import tabulate

class SearchSubjectGUI:
    def __init__(self):
        self.__sjBLL = SubjectBLL()

    def openScreen(self):
        print('*** Search Subject by text ***')
        text = input('Noi dung tim kiem: ')
        result = self.__sjBLL.search(text)
        if len(result)>0:
            print(tabulate(result,headers=('SubjectCode','Subjectname')))
        else:
            print("Không tìm thấy môn học")