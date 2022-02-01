import code
from tabnanny import check
from unittest import result

from numpy import full
from bll import ScoreBLL
from bll import StudentBLL
from bll import SubjectBLL
from dto import ScoreDto

class AddScoreGUI:
    def __init__(self):
        self.__stBLL = StudentBLL()
        self.__sjBLL = SubjectBLL()
        self.__scBLL = ScoreBLL()
    
    def existCode(self):
        a=self.__stBLL.getAll()
        while True:
            self.Code = input('Ma HV: ')
            if self.Code=='':
                print('Không được để trống Mã HV !')
                continue 
            if len(self.Code)!=8:
                print("Mã sinh viên cần 8 kí tự")
                continue
            for i in a:
                if i[0]==self.Code:
                    print(f"Mã sinh viên {self.Code}")
                    return self.Code 
            print("Mã sinh viên không tồn tại")

    def existCodej(self):
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
    
    def addScoreQT(self):
        while True:
            a= int(input("Score QT:"))
            if a in range(0,101):
                return(a)
            else:
                print("Điểm số nằm chỉ từ 0 đến 100")
                continue
    def addScoreKT(self):
        while True:
            a= int(input("Score KT:"))
            if a in range(0,101):
                return(a)
            else:
                print("Điểm số nằm chỉ từ 0 đến 100")
                continue

    def openScreen(self):
        print('*** Add a new Score ***')
        studentCode = self.existCode()
        subjectCode = self.existCodej()
        scoreQT = self.addScoreQT()
        scoreKT = self.addScoreKT()
        
        scDto = ScoreDto(studentCode, subjectCode, scoreQT,scoreKT)
        result = self.__scBLL.insert(scDto)
        if result==0:
            print("-----error-----")
        if result==1:
            print("-----Done-----")
    
