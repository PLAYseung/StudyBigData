import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

# class OOP
class qTemplate(QWidget):

    # 생성자
    def __init__(self) -> None: # -> None 리턴 값이 없다 ( 생성자는 기본적으로 리턴값이 없음 ) Str : 문자열 반환 해야한다
        super().__init__()
        self.initUI()

    # 화면 정의를 위해서 만드 사용자 함수
    def initUI(self):
        self.addControls()
        self.setGeometry(300,200,320,230)
        self.setWindowTitle('QPushButton')
        self.show()

    def addControls(self):
        btn01 = QPushButton('click', self)
        btn01.setGeometry(100, 100, 100, 40)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()