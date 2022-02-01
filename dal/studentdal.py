from .dbprovider import DBProvider

from dto import StudentDto


class StudentDAL:
    def __init__(self):
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()

    #thêm học viên
    def insert(self, st: StudentDto):
        sql = """
            INSERT INTO Student(Code, FullName, Birthday, Sex, Address, Phone, Email)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        val = (st.code, st.fullName, st.birthDay, st.sex, st.address, st.phone, st.email) # Cast object from Student to tuple
        return self.__dbProvider.exec(sql, val)

    #update học viên
    def update(self, st: StudentDto):
        sql = """
            UPDATE Student
            SET FullName = %s,
                Birthday = %s,
                Sex = %s,
                Address = %s,
                Phone = %s,
                Email = %s
            WHERE Code = %s
        """
        val = (st.fullName, st.birthDay, st.sex, st.address, st.phone, st.email, st.code)
        return self.__dbProvider.exec(sql, val)

    #xóa học viên
    def delete(self, st: StudentDto):
        sql = """
            DELETE FROM Student
            WHERE Code = %s
        """
        val = (st.code,)
        return self.__dbProvider.exec(sql, val)

    #lấy ra thông tin
    def getAll(self):
        sql = """
            SELECT Code, FullName, Birthday, Sex, Address, Phone, Email
            FROM Student
        """
        return self.__dbProvider.get(sql) #gọi get()để in ra
    #lấy ra 1 thông tin
    def getByCode(self, code: str):
        sql = """
            SELECT Code, FullName, Birthday, Sex, Address, Phone, Email
            FROM Student
            WHERE Code = %s
        """
        val = (code,)
        return self.__dbProvider.getOne(sql, val)#in ra 1 bản

    #tìm kiếm học viên
    def search(self, text: str):
        sql = """
            SELECT Code, FullName, Birthday, Sex, Address, Phone, Email
            FROM Student
            WHERE Code = %s
                OR FullName LIKE %s
                OR Email LIKE %s
        """
        params = (text, f'%{text}%', f'%{text}%')
        return self.__dbProvider.get(sql, params)

    #tạo bảng nếu không tồn tại
    def __createTableIfNotExists(self):
        sql = """
            CREATE TABLE IF NOT EXISTS Student(
                Code VARCHAR(8) PRIMARY KEY,
                FullName NVARCHAR(50),
                Birthday VARCHAR(20),
                Sex TINYINT(1),
                Address NVARCHAR(500),
                Phone VARCHAR(20),
                Email VARCHAR(250)
            )
        """
        self.__dbProvider.exec(sql)
    
    

       