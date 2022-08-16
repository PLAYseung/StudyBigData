import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# class OOP
class qTemplate(QWidget):

    # 생성자
    def __init__(self) -> None: # -> None 리턴 값이 없다 ( 생성자는 기본적으로 리턴값이 없음 ) Str : 문자열 반환 해야한다
        super().__init__()
        uic.loadUi('./pyQt02/ttask.ui',self)
        self.initUI()

    # 화면 정의를 위해서 만드 사용자 함수
    def initUI(self):
        self.addControls()
        self.show()


    def addControls(self):
        self.btnStart.clicked.connect(self.btn1_clicked) # 시그널 연결
    
    def btn1_clicked(self):
        self.txbLog.append('실행!!')
        self.pgbTask.setRange(0,99)
        for i in range(0,100):
            print(f'출력 : {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'출력 > {i}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()