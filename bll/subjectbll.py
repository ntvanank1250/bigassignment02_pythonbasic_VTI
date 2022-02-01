from dal import SubjectDAL
from dto import SubjectDto


class SubjectBLL:
    def __init__(self):
        self.__sjDAL = SubjectDAL()

    def insert(self, sj: SubjectDto):
        return self.__sjDAL.insert(sj)

    def update(self, sj: SubjectDto):
        return self.__sjDAL.update(sj)

    def delete(self, code: str):
        return self.__sjDAL.delete(code)

    def getAll(self):
        return self.__sjDAL.getAll()

    def getByCode(self, code: str):
        return self.__sjDAL.getByCode(code)

    def search(self, text: str):
        return self.__sjDAL.search(text)