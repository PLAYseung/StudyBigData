import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QIcon
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
        self.setWindowTitle('Qlabel')
        self.show()

    def addControls(self):
        self.setWindowIcon(QIcon('./pyQt01/data/lion.png'))
        label1 = QLabel('label 1',self)
        label2 = QLabel('label 2',self)
        label1.setStyleSheet(
            (
                'border-width : 3px;'
                'border-style : solid;'
                'border-color : blue;'
                'image : url(./pyQt01/data/image1.png)'
            )
        )
        label2.setStyleSheet(
            (
                'border-width : 3px;'
                'border-style : dot-dot-dash;'
                'border-color : red;'
                'image : url(./pyQt01/data/image2.png)'
            )
        )

        box = QHBoxLayout()
        box.addWidget(label1)
        box.addWidget(label2)        

        self.setLayout(box)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()