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
        
        self.label = QLabel('메시지 :',self)
        self.label.setGeometry(10,10,600,40)
        btn01.setGeometry(100, 100, 100, 40)
        btn01.clicked.connect(self.btn1_clicked) # 시그널 연결
    
    def btn1_clicked(self):
        # QMessageBox.information(self,'signal','btn1_clicked') # 정보
        # QMessageBox.warning(self,'signal','btn1_clicked') # 경고
        self.label.setText('메시지 : btn01 버튼 클릭')
        QMessageBox.critical(self,'signal','btn1_clicked') # 에러
        # QMessageBox(icon, title, text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()