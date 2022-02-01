from bll import SubjectBLL
from dto import SubjectDto


class DeleteSubjectGUI:
    def __init__(self):
        self.__sjBLL = SubjectBLL()

    def existCode(self):
        a=self.__sjBLL.getAll()
        while True:
            self.Code = input('Mã môn học: ')
            if self.Code=='':
                print('Không được để trống mã môn học !')
                continue 
            for i in a:
                if i[0]==self.Code:
                    print(f"Mã môn học {self.Code}")
                    return self.Code 
            print("Mã môn học không tồn tại")
    
    def openScreen(self):
        print('*** Delete a Subject by Code ***')
        code = self.existCode()
        result = self.__sjBLL.delete(code)
        if result==0:
            print("-----error-----")
        if result==1:
            print("-----Done-----")
