import random
from functools import partial
import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

# def get_rand_number():
#     list = []
#     i=0
#     while i<16:
#         r=random.randint
#         if r in list:
#             r=random.randint(1,16)
#         else:
#             list.append(r)
#     return list
            

 

def get_rand_number():
    list = []

    for i in range(16):
        r=random.randint(1,16)
        while r in list:
            r=random.randint(1,16)

        list.append(r)
    return list


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.buttons=[[self.ui.btm1,self.ui.btm2,self.ui.btm3,self.ui.btm4],
                    [self.ui.btm5,self.ui.btm6,self.ui.btm7,self.ui.btm8],
                    [self.ui.btm9,self.ui.btm10,self.ui.btm11,self.ui.btm12],
                    [self.ui.btm13,self.ui.btm14,self.ui.btm15,self.ui.btm16]]

        my_list=get_rand_number()
        m=0
        for i in range(4):
            for j in range(4):
                r = my_list[m]
                self.buttons[i][j].setText(str(r))
                m+=1
                self.buttons[i][j].clicked.connect(partial(self.play , i ,j))
                if r==16:
                    self.buttons[i][j].setVisible(False)
                    self.empty_i=i
                    self.empty_j=j

    def play(self,i ,j):
        if (i==self.empty_i and (j==self.empty_j-1 or j==self.empty_j+1)) or (j==self.empty_j and (i==self.empty_i-1 or i==self.empty_i+1)):
            self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].text())
            self.buttons[self.empty_i][self.empty_j].setVisible(True)
            self.buttons[i][j].setText("16")
            self.buttons[i][j].setVisible(False)
            self.empty_i=i
            self.empty_j=j

        if self.check_win()==True:
            msg_box=QMessageBox()
            msg_box.setText("You Win")
            msg_box.exec()


    def check_win(self):
        index=1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text()) != index:
                    return False
                index+=1
        return True  




app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()

app.exec()