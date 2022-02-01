from .dbprovider import DBProvider

from dto import ScoreDto
import openpyxl

class ScoreDAL:
    def __init__(self):
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()

    #thêm diem so
    def insert(self, sc: ScoreDto):
        sql = """
            INSERT INTO Score(StudentCode, SubjectCode, ScoreQT, ScoreKT)
            VALUES (%s, %s, %s, %s)
        """
        val = (sc.studentCode, sc.subjectCode, sc.scoreQT, sc.scoreKT) 
        return self.__dbProvider.exec(sql, val)

    #update diem so
    def update(self, sc: ScoreDto):
        sql = """
            UPDATE Score
            SET ScoreQT = %s,
                ScoreKT = %s
            WHERE StudentCode = %s
            AND SubjectCode= %s
        """
        val = (sc.scoreQT, sc.scoreKT, sc.studentCode, sc.subjectCode)
        return self.__dbProvider.exec(sql, val)

    #xóa diem so
    def delete(self, studentCode: str,subjectCode: str):
        sql = """
            DELETE FROM Score
            WHERE StudentCode = %s
            AND SubjectCode =%s
        """
        val = (studentCode,subjectCode)
        return self.__dbProvider.exec(sql, val)

    #lấy ra thông tin
    def getAll(self):
        sql = """
            SELECT StudentCode, SubjectCode, ScoreQT, ScoreKT
            FROM Score
        """
        return self.__dbProvider.get(sql) #gọi get()để in ra
    #lấy ra 1 thông tin
    def getByCode(self, studentCode: str,subjectCode: str):
        sql = """
            SELECT StudentCode, SubjectCode, ScoreQT, ScoreKT
            FROM Score
            WHERE StudentCode = %s
            AND SubjectCode= %s
        """
        val = (studentCode,subjectCode)
        return self.__dbProvider.getOne(sql, val)#in ra 1 bản

    #tìm kiếm học viên
    def search(self, text: str):
        sql = """
            SELECT sc.StudentCode,st.FullName, sc.SubjectCode, sc.ScoreQT, sc.ScoreKT
            FROM Score sc
            JOIN Student st
            ON sc.StudentCode=st.Code
            WHERE sc.StudentCode like %s
            OR st.FullName like %s        
        """
        params = (f'%{text}%',f'%{ text}%')
        return self.__dbProvider.get(sql, params)

    
    def getScore(self):
        sql="""
        SELECT sc.StudentCode,st.FullName,st.Birthday,st.Phone,st.Email,sj.SubjectCode,sc.ScoreQT,sc.ScoreKT,(sc.Scoreqt + sc.Scorekt*2)/3 as Scoretk,
        CASE
	        WHEN (sc.scoreqt + sc.scorekt*2)/3>=90 THEN "A"
            WHEN (sc.scoreqt + sc.scorekt*2)/3>=70 THEN "B"
            WHEN (sc.scoreqt + sc.scorekt*2)/3>=50 THEN "C"
            else "D"
        END AS Grage
        FROM score sc
        JOIN student st 
        ON st.Code = sc.StudentCode
        JOIN `subject` sj
        ON sc.SubjectCode=sj.SubjectCode
        """
        return self.__dbProvider.get(sql) 
        
    def output_Excel(self,input_detail):
        output_excel_path= 'C:/Users/Admin/Desktop/Score.xlsx'
    #Xác định số hàng và cột lớn nhất trong file excel cần tạo
        row = len(input_detail)
        column = len(input_detail[0])

        #Tạo một workbook mới và active nó
        wb = openpyxl.Workbook()
        ws = wb.active
        
        #Dùng vòng lặp for để ghi nội dung từ input_detail vào file Excel
        for i in range(0,row):
            for j in range(0,column):
                v=input_detail[i][j]
                ws.cell(column=j+1, row=i+1, value=v)

        #Lưu lại file Excel
        wb.save(output_excel_path)

        #tạo bảng nếu không tồn tại
    def __createTableIfNotExists(self):
        sql = """
            CREATE TABLE IF NOT EXISTS Score(
                StudentCode VARCHAR(8),
                SubjectCode VARCHAR(8),
                ScoreQT TINYINT DEFAULT 0,
                ScoreKT TINYINT DEFAULT 0
            )
        """
        # TODO Primary key contrains
        self.__dbProvider.exec(sql)

       