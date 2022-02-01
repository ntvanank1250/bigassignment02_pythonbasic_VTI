import code
from tabnanny import check
from unittest import result

from numpy import full
from bll import SubjectBLL
from dto import SubjectDto


class AddSubjectGUI:
    def __init__(self):
        self.__sjBLL = SubjectBLL()

    def addCode(self):
        a=self.__sjBLL.getAll()
        while True:
            self.Code = input('Ma MH: ')
            if self.Code=='':
                print('Không được để trống Mã MH !')
                continue 
            
            flag=1
            for i in a:
                if i[0]==self.Code:
                    print("Mã môn học đã tồn tại")
                    flag=0
            if flag==0:
                continue
            break
        print(f"{self.Code} is OK")
        return self.Code 

    def addSubjectName(self):
        return input("Subject name:")

    def existCode(self):
        a=self.__sjBLL.getAll()
        while True:
            self.Code = input('Ma MH: ')
            if self.Code=='':
                print('Không được để trống Mã MH !')
                continue 
            for i in a:
                if i[0]==self.Code:
                    print(f"Mã môn học {self.Code}")
                    return self.Code 
            print("Mã môn học không tồn tại")
    

    def openScreen(self):
        print('*** Add a new student ***')
        code = self.addCode()
        subjectName = self.addSubjectName()
        
        sjDto = SubjectDto(code, subjectName)
        result = self.__sjBLL.insert(sjDto)
        if result==0:
            print("-----error-----")
        if result==1:
            print("-----Done-----")