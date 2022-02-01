from dal import StudentDAL
from dto import StudentDto
import re
import datetime

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class StudentBLL:
    def __init__(self):
        self.__stDAL = StudentDAL()

    def insert(self, st: StudentDto):
        return self.__stDAL.insert(st)

    def update(self, st: StudentDto):
        return self.__stDAL.update(st)

    def delete(self, st: StudentDto):
        return self.__stDAL.delete(st)

    def getAll(self):
        return self.__stDAL.getAll()

    def getByCode(self, code: str):
        return self.__stDAL.getByCode(code)

    def search(self, text: str):
        return self.__stDAL.search(text)
    
    
    
    
    