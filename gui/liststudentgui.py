from bll import StudentBLL
from dto import StudentDto
from tabulate import tabulate

class ListStudentGUI:
    def __init__(self):
        self.__stBLL = StudentBLL()

    def openScreen(self):
        print('*** List of students ***')
        result = self.__stBLL.getAll()
        
        print(tabulate(result, headers=('Code','Fullname','Birthday','Sex','Địa chỉ','Phone','Email')))
     
