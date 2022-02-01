from bll import StudentBLL
from dto import StudentDto


class DeleteStudentGUI:
    def __init__(self):
        self.__stBLL = StudentBLL()
        
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

    def openScreen(self):
        print('*** Delete a student by Code ***')
        code = self.existCode()
        stDto = StudentDto(code,'','','','','','')
        result = self.__stBLL.delete(stDto)

        if result==0:
            print("-----error-----")
        if result==1:
            print("-----Done-----")