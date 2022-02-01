from bll import ScoreBLL
from bll import StudentBLL
from bll import SubjectBLL
from dto import ScoreDto
from tabulate import tabulate

class SearchScoreGUI:
    def __init__(self):
        self.__stBLL = StudentBLL()
        self.__sjBLL = SubjectBLL()
        self.__scBLL = ScoreBLL()

    def openScreen(self):
        print('*** Search score by text ***')
        x=input("Nhập mã cần tìm kiếm:")
        result = self.__scBLL.search(x)
        if len(result)>0:
            print(tabulate(result,headers=('StudentCode','FullName','SubjectCode','ScoreQT','ScoreKT')))
        else:
            print("Không tìm thấy Điểm thi")