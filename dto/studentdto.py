#truyền và gán giá trị cho học viên
class StudentDto:
    def __init__(self, code: str, fullName: str, birthDay: str, sex: int, address: str, phone: str, email: str):
        self.code = code
        self.fullName = fullName
        self.birthDay = birthDay
        self.sex = sex
        self.address = address
        self.phone = phone
        self.email = email
