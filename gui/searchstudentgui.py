from bll import StudentBLL
from dto import StudentDto
from tabulate import tabulate

class SearchStudentGUI:
    def __init__(self):
        self.__stBLL = StudentBLL()

    def openScreen(self):
        print('*** Search student by text ***')
        text = input('Noi dung tim kiem: ')
        result = self.__stBLL.search(text)
        if len(result)>0:
            print(tabulate(result,headers=('Code','Fullname','Birthday','Sex','Địa chỉ','Phone','Email')))
        else:
            print("Không tìm thấy học viên")