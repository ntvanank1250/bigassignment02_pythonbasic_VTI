import code
from tabnanny import check
from unittest import result
import re
import datetime

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

from numpy import full
from bll import StudentBLL
from dto import StudentDto

class AddStudentGUI:
    def __init__(self):
        self.__stBLL = StudentBLL()
        
    def addCode(self):
        a=self.__stBLL.getAll()
        while True:
            self.Code = input('Ma HV: ')
            if self.Code=='':
                print('Không được để trống Mã HV !')
                continue 
            if len(self.Code)!=8:
                print("Mã sinh viên cần 8 kí tự")
                continue
            flag=1
            for i in a:
                if i[0]==self.Code:
                    print("Mã sinh viên đã tồn tại")
                    flag=0
            if flag==0:
                continue
            break
        print(f"{self.Code} is OK")
        return self.Code 
    
    def addFullName(self):
        return input("Full name:")

    def addBirthDay(self):
        while True:
            birthday = input('Ngay sinh (DD/MM/YYYY): ')
            try:
                datetime.datetime.strptime(birthday, '%d/%m/%Y')
                return birthday
            except:
                print("Nhập sai ngày tháng, mời bạn nhập lại!")
                continue

    def addSex(self):
        while True:
            sex=input("Nhập giới tính 0-nữ |1-nam:")
            if sex not in ('1','0'):
                print("Nhập sai giới tính")
                continue
            return int(sex)

    def addAddress(self):
        return input("Địa chỉ:")

    def addPhone(self):
        while True:
            phone=input("Nhập số điện thoại:")
            a=self.__stBLL.getAll()
            flag=1
            for i in a:
                if i[5]==phone:
                    print("Phone đã tồn tại")
                    flag=0
            if flag==0:
                continue
            b=("1","2","3","4","5","6","7","8","9","0")
            type_phone=True
            for i in range(1,len(phone)):
                if phone[i] not in b:
                    type_phone=False
                    continue
            if 9>=len(phone) or len(phone)>=13 or type_phone==False:
                print("Số điện thoại không đúng, yêu cầu nhập lại")
                continue
            if phone[0]!='0' and phone[0]!='+' and phone[0]!='8':
                print("Số điện thoại không đúng, yêu cầu nhập lại:")
                continue
            return phone

    def addEmail(self):

        while True:
            email=input("Nhập email:")
            a=self.__stBLL.getAll()
            flag=1
            for i in a:
                if i[6]==email:
                    print("Email đã tồn tại")
                    flag=0
            if flag==0:
                continue
            if(re.fullmatch(regex, email)):
                return email
            else:
                print("Nhập sai Gmail, yêu cầu nhập lại")
                continue

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
        print('*** Add a new student ***')
        code = self.addCode()
        fullName = self.addFullName()
        birthday = self.addBirthDay()
        sex = self.addSex()
        address = self.addAddress()
        phone = self.addPhone()
        email = self.addEmail()
        stDto = StudentDto(code, fullName, birthday,
                           sex, address, phone, email)
        result = self.__stBLL.insert(stDto)
        if result==0:
            print("-----error-----")
        if result==1:
            print("-----Done-----")
    
