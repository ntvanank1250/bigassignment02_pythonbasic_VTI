from .dbprovider import DBProvider

from dto import SubjectDto


class SubjectDAL:
    def __init__(self):
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()

    #thêm học viên
    def insert(self, sj: SubjectDto):
        sql = """
            INSERT INTO Subject(SubjectCode, SubjectName)
            VALUES (%s, %s)
        """
        val = (sj.subjectCode, sj.subjectName) # Cast object from Subject to tuple
        return self.__dbProvider.exec(sql, val)

    #update học viên
    def update(self, sj: SubjectDto):
        sql = """
            UPDATE Subject
            SET SubjectName = %s
            WHERE SubjectCode = %s
        """
        val = (sj.subjectName, sj.subjectCode)
        return self.__dbProvider.exec(sql, val)

    #xóa học viên
    def delete(self, code: str):
        sql = """
            DELETE FROM Subject
            WHERE SubjectCode = %s
        """
        val = (code,)
        return self.__dbProvider.exec(sql, val)

    #lấy ra thông tin
    def getAll(self):
        sql = """
            SELECT SubjectCode, SubjectName
            FROM Subject
        """
        return self.__dbProvider.get(sql) #gọi get()để in ra
    #lấy ra 1 thông tin
    def getByCode(self, code: str):
        sql = """
            SELECT SubjectCode, SubjectName
            FROM Subject
            WHERE SubjectCode = %s
        """
        val = (code,)
        return self.__dbProvider.getOne(sql, val)#in ra 1 bản

    #tìm kiếm học viên
    def search(self, text: str):
        sql = """
            SELECT SubjectCode, SubjectName
            FROM Subject
            WHERE SubjectCode = %s
                OR SubjectName LIKE %s
        """
        params = (text, f'%{text}%')
        return self.__dbProvider.get(sql, params)

    #tạo bảng nếu không tồn tại
    def __createTableIfNotExists(self):
        sql = """
            CREATE TABLE IF NOT EXISTS Subject(
                SubjectCode VARCHAR(30) PRIMARY KEY,
                SubjectName NVARCHAR(50)
            )
        """
        self.__dbProvider.exec(sql)
    


       