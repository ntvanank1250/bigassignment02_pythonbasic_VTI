from shutil import move
from gui import *

class Menu: 
    def __init__(self) -> None:
        #Học viên
        self.addStudentGUI = AddStudentGUI()   
        self.deleteStudentGui= DeleteStudentGUI()
        self.listStudentGui=ListStudentGUI()
        self.searchStudentGUI=SearchStudentGUI()
        self.upDateStudentGUI=UpdateStudentGUI()
        #Môn học
        self.addSubjectGUI = AddSubjectGUI()   
        self.deleteSubjectGui= DeleteSubjectGUI()
        self.listSubjectGui=ListSubjectGUI()
        self.searchSubjectGUI=SearchSubjectGUI()
        self.upDateSubjectGUI=UpdateSubjectGUI()
        #điểm số
        self.addScoreGUI = AddScoreGUI()   
        self.deleteScoreGui= DeleteScoreGUI()
        self.listScoreGui=ListScoreGUI()
        self.searchScoreGUI=SearchScoreGUI()
        self.upDateScoreGUI=UpdateScoreGUI()
        self.printScoreGUI=PrintScoreGUI()
    #màn hình chính
    def menuMain(self):
        a=["[1] Quản lý thông tin Học viên",
        "[2] Quản lý thông tin Môn học",
        "[3] Quản lý thông tin Điểm thi",
        "[4] Kết Xuất Bảng Điểm"]
        for i in a:
            print(i)
        while True:
            x=input("Lựa chọn:")
            print('*'*30)
            if x=='1':
                self.studentMain()
            if x=='2':
                self.subjectMain()
            if x=='3':
                self.scoreMain()
            if x=='4':
                self.printMain()
            else:
                print("Nhập sai giá trị")
                continue
    #màn hình quản lý sinh viên
    def studentMain(self):
        a=["[1] Thêm Học viên",
        "[2] Xóa học viên",
        "[3] Liệt kê danh sách học viên",
        "[4] Tìm kiếm học viên",
        "[5] Sửa thông tin học viên",
        "[0] Để quay về màn hình chính"]
        for i in a:
            print(i)
        while True:
            x=input("Lựa chọn:")
            print('*'*30)
            if x=='1':
                self.addStudentGUI.openScreen()
                break
            if x=='2':
                self.deleteStudentGui.openScreen()
                break
            if x=='3':
                self.listStudentGui.openScreen()
                break
            if x=='4':
                self.searchStudentGUI.openScreen()
                break
            if x=='5':
                self.upDateStudentGUI.openScreen()
                break
            if x=='0':
                self.menuMain()
            else:
                print("Nhập sai giá trị")
                continue
        self.moveMenu()  
    #màn hình quản lý môn học
    def subjectMain(self):
        a=["[1] Thêm Môn học",
        "[2] Xóa môn học",
        "[3] Liệt kê danh sách môn học",
        "[4] Tìm kiếm môn học",
        "[5] Sửa thông tin môn học",
        "[0] Để quay về màn hình chính"]
        for i in a:
            print(i)
        while True:
            x=input("Lựa chọn:")
            print('*'*30)
            if x=='1':
                self.addSubjectGUI.openScreen()
                break
            if x=='2':
                self.deleteSubjectGui.openScreen()
                break
            if x=='3':
                self.listSubjectGui.openScreen()
                break
            if x=='4':
                self.searchSubjectGUI.openScreen()
                break
            if x=='5':
                self.upDateSubjectGUI.openScreen()
                break
            
            if x=='0':
                self.menuMain()
            else:
                print("Nhập sai giá trị")
                continue
        self.moveMenu()  
    #màn hình quản lý điểm
    def scoreMain(self):
        a=["[1] Thêm điểm số",
        "[2] Xóa điểm số",
        "[3] Liệt kê danh sách điểm số",
        "[4] Tìm kiếm điểm số",
        "[5] Sửa điểm số",
        "[0] Để quay về màn hình chính"]
        for i in a:
            print(i)
        while True:
            x=input("Lựa chọn:")
            print('*'*30)
            if x=='1':
                self.addScoreGUI.openScreen()
                break
            if x=='2':
                self.deleteScoreGui.openScreen()
                break
            if x=='3':
                self.listScoreGui.openScreen()
                break
            if x=='4':
                self.searchScoreGUI.openScreen()
                break
            if x=='5':
                self.upDateScoreGUI.openScreen()
                break
            if x=='0':
                self.menuMain()
            else:
                print("Nhập sai giá trị")
                continue
        self.moveMenu()
    #lựa chọn kết xuất điểm
    def printMain(self):
        a=["[1] In tất cả học viên",
            "[2] In học viên đạt A",
            "[3] In học viên đạt B",
            "[4] In học viên đạt C",
            "[5] In học viên đạt D",
            "[0] Để quay về màn hình chính"]
        for i in a:
            print(i)
        while True:
            x=input("Lựa chọn:")
            print('*'*30)
            if x=='1':
                self.printScoreGUI.openScreen()
                break
            if x=='2':
                self.printScoreGUI.openScreenA()
                break
            if x=='3':
                self.printScoreGUI.openScreenB()
                break
            if x=='4':
                self.printScoreGUI.openScreenC()
                break
            if x=='5':
                self.printScoreGUI.openScreenD()
                break
            if x=='0':
                self.menuMain()
            else:
                print("Nhập sai giá trị")
                continue
        self.moveMenu()  
    #lựa chọn thoát chương trình
    def moveMenu(self):
        a=["[0] Để thoát chương trình",
        "[1] Quay lại menu chính"]
        for i in a:
            print(i)
        while True:
            x=input("Lựa chọn:")
            print('*'*30)
            if x=='0':exit()
            
            if x=='1':self.menuMain()
            else:
                print("Nhập sai giá trị")
                continue

if __name__ == '__main__':
    
    Menu().menuMain()
    
    