from bll import ScoreBLL
from dto import ScoreDto
from tabulate import tabulate

class PrintScoreGUI:
    def __init__(self):
        self.__scBLL = ScoreBLL()
        self.header=[('StudentCode','FullName','Birthday','Phone','Email','SubjectCode','ScoreQT','ScoreKT','Scoretk','Grage')]
    def openScreen(self):
        input_detail= self.header + self.__scBLL.getScore()
        print (tabulate(input_detail))
        self.__scBLL.output_Excel(input_detail)
    def openScreenA(self):
        input_detail= self.header 
        a=self.__scBLL.getScore()
        for i in a:
            if i[9]=='A':
                input_detail+=[(i)]
        print (tabulate(input_detail))
        self.__scBLL.output_Excel(input_detail)
    def openScreenB(self):
        input_detail= self.header 
        a=self.__scBLL.getScore()
        for i in a:
            if i[9]=='B':
                input_detail+=[(i)]
        print (tabulate(input_detail))
        self.__scBLL.output_Excel(input_detail)
    def openScreenC(self):
        input_detail= self.header 
        a=self.__scBLL.getScore()
        for i in a:
            if i[9]=='C':
                input_detail+=[(i)]
        print (tabulate(input_detail))
        self.__scBLL.output_Excel(input_detail)
    def openScreenD(self):
        input_detail= self.header 
        a=self.__scBLL.getScore()
        for i in a:
            if i[9]=='D':
                input_detail+=[(i)]
        print (tabulate(input_detail))
        self.__scBLL.output_Excel(input_detail)        