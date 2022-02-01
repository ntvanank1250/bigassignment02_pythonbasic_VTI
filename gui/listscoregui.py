from bll import ScoreBLL
from bll import StudentBLL
from bll import SubjectBLL
from dto import ScoreDto
from tabulate import tabulate


class ListScoreGUI:
    def __init__(self):
        self.__stBLL = StudentBLL()
        self.__sjBLL = SubjectBLL()
        self.__scBLL = ScoreBLL()

    def openScreen(self):
        print('*** List of score ***')
        result = self.__scBLL.getScore()
        print(tabulate(result, headers=('StudentCode','FullName','Birthday','Phone','Email','SubjectCode','ScoreQT','ScoreKT','Scoretk','Grage')))
