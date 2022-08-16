import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

# UI 스레드와 작업 스레드를 분리
class Worker(QThread):
    # QThread는 화면을 그릴 권한이 없음
    # 통신을 통해서 UI스레드가 그림을 그릴 수 있도록 해줌
    valChangeSignal = pyqtSignal(int)

    def __init__(self, parant):
        super().__init__(parant)
        self.parent = parant
        self.working = True # 클래스 내부변수 working을 지정

    def run(self):
        # 스레드로 동작할 내용
        while self.working:
            for i in range(0,100000):
                print(f'출력 : {i}')
                # self.pgbTask.setValue(i)
                # self.txbLog.append(f'출력 > {i}')
                self.valChangeSignal.emit(i) # 화면은 ui 스래드가 그려준다
                time.sleep(0.0001)




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
        # worker 클래스 생성
        self.worker = Worker(self)
        self.worker.valChangeSignal.connect(self.updateProgress) # 스래드애서 받은 시그널
        # updateProgress 함수에서 처리해줌
    
    @pyqtSlot(int)
    def updateProgress(self,val): # val이 Worker스레드에서 전달 받은 반복갑
        self.pgbTask.setValue(val)
        self.txbLog.append(f'출력 > {val}')
        if val == 99999:
            self.worker.working = False
    
    def btn1_clicked(self):
        self.txbLog.append('실행!!')
        self.pgbTask.setRange(0,99999)
        self.worker.start()
        self.worker.working=True
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()