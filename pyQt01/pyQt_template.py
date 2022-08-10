import sys
from PyQt5.QtWidgets import QApplication,QWidget

# class OOP
class qTemplate(QWidget):

    # 생성자
    def __init__(self) -> None: # -> None 리턴 값이 없다 ( 생성자는 기본적으로 리턴값이 없음 ) Str : 문자열 반환 해야한다
        super().__init__()
        self.initUI()

    '''
    def __init__ ...
    스페셜 메서드 : 함수 명에 '__()__' 가 들어 가는 함수
    '''

    def initUI(self):
        self.setGeometry(300,200,320,230)
        self.setWindowTitle('QFont')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()