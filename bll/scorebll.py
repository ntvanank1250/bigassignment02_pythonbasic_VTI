from dal import ScoreDAL
from dto import ScoreDto





class ScoreBLL:
    def __init__(self):
        self.__scDAL = ScoreDAL()
    def insert(self, sc: ScoreDto):
        return self.__scDAL.insert(sc)

    def update(self, sc: ScoreDto):
        return self.__scDAL.update(sc)

    def delete(self, x:str,y:str):
        return self.__scDAL.delete(x,y)

    def getAll(self):
        return self.__scDAL.getAll()

    def getByCode(self, x:str,y:str):
        return self.__scDAL.getByCode(x,y)

    def search(self, x:str):
        return self.__scDAL.search(x)

    def getScore(self):
        return self.__scDAL.getScore()

    def output_Excel(self,input_detail):
        self.__scDAL.output_Excel(input_detail)