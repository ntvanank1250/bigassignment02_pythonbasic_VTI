from turtle import update
from bll import SubjectBLL
from dto import SubjectDto


class UpdateSubjectGUI:
    def __init__(self):
        self.__sjBLL = SubjectBLL()

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
        print('*** Update a Subject ***')
        subjectCode = self.existCode()
        subjectName = self.addSubjectName()
        stDto = SubjectDto(subjectCode, subjectName)
        result = self.__sjBLL.update(stDto)
        if result==0:
            print("-----error-----")
        if result==1:
            print("-----Done-----")
