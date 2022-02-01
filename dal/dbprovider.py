from turtle import pen
import mysql.connector

class DBProvider:
    def __init__(self):
        # Khoi tao thong tin ket noi toi MySQL
        self.host = "127.0.0.1"
        self.user = "root"
        self.passwd = "1250"
        self.db = "testdb"
        self.conn = None
        self.cur = None

    # Ket noi toi MySQL
    def connect(self):
        try:
            self.conn = mysql.connector.connect(host=self.host,
                                                user=self.user,
                                                passwd=self.passwd,
                                                db=self.db)
            self.cur = self.conn.cursor()
        except:
            print("Không thể kết nối tới database")
 

    # Dong ket noi
    def close(self):
        try:
            if self.conn is not None:
                self.conn.close()
                self.conn = None
                self.cur = None
        except:
            print("Không thể đóng database")
            
    # Execute => Thay doi du lieu
    def exec(self, sql: str, *params):
        rowCount = 0
        try:
            self.connect()
            self.cur.execute(sql, *params)
            self.conn.commit()
            rowCount = self.cur.rowcount
        except Exception as e:
            print(e)
        finally:
            self.close()
        return rowCount

    # Get many => Lay nhieu ban ghi thành 1 cái tuple trong list
    def get(self, sql: str, *params):
        self.connect()

        self.cur.execute(sql, *params)
        result = [row for row in self.cur.fetchall()]

        self.close()
        
        return result
        
    # Get one => Lay 1 ban ghi
    def getOne(self, sql: str, *params):
        self.connect()

        self.cur.execute(sql, *params)
        result = self.cur.fetchone()

        self.close()
        return result
