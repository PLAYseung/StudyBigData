import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt

# class OOP
class qTemplate(QWidget):

    # 생성자
    def __init__(self) -> None: # -> None 리턴 값이 없다 ( 생성자는 기본적으로 리턴값이 없음 ) Str : 문자열 반환 해야한다
        super().__init__()
        self.initUI()

    # 화면 정의를 위해서 만드 사용자 함수
    def initUI(self):
        self.setGeometry(300,200,320,230)
        self.setWindowTitle('QTitle')
        self.text = 'QFont hello world'
        self.show()

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        self.drawText(event,paint)
        paint.end()

    # 텍스트를 그리기 위한 사용자 정의 함수
    def drawText(self,event,paint):
        paint.setPen(QColor(255,255,255))
        paint.setFont(QFont('H2GTRM',20))
        paint.drawText(50,50,'Hell World')  # QPainter에 있는 내장 함수
        paint.setPen(QColor(00,250,00))
        paint.setFont(QFont('H2GTRM',10))
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()