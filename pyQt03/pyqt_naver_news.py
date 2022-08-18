import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from urllib.parse import quote
import urllib.request
import json
import webbrowser
import pandas as pd # csv 저장용

# class OOP
class qTemplate(QWidget):
    start = 1 # api 호출할 때 시작하는 데이터 번호
    max_display = 100 # 한 페이지에 나올 데이터 수
    saveResult = [] # 저장할 때 담을 데이터(딕셔너리 리스트) -> DataFrame

    # 생성자
    def __init__(self) -> None: # -> None 리턴 값이 없다 ( 생성자는 기본적으로 리턴값이 없음 ) Str : 문자열 반환 해야한다
        super().__init__()
        uic.loadUi('./pyQt03/navernews_2.ui',self)
        self.initUI()

    # 화면 정의를 위해서 만드 사용자 함수
    def initUI(self):
        self.addControls()
        self.show()

    def addControls(self):  # 위젯 정의, 이벤트(시그널) 처리
        self.btnSearch.clicked.connect(self.btnSearchClikcked)
        self.txtSearch.returnPressed.connect(self.btnSearchClikcked)
        self.tblResult.itemSelectionChanged.connect(self.tblResultSelected)

        # 22.08.18 추가버튼 이벤트(시그널) 확장
        self.btnNext.clicked.connect(self.btnNextClicked)
        self.btnSave.clicked.connect(self.btnSaveClicked)

    def btnNextClicked(self):
        self.start = self.start+self.max_display
        self.btnSearchClikcked()

    def btnSaveClicked(self):
        if len(self.saveResult)>0:
            df = pd.DataFrame(self.saveResult)
            df.to_csv(f'./pyQt03/{self.txtSearch.text()}_뉴스검색결과.csv',encoding='utf-8',index=True)

        QMessageBox.information(self, '저장', '저장완료!')
        # 저장후 모든 변수 초기화
        self.saveResult = []
        self.start = 1
        self.txtSearch.setText('')
        self.lblStatus.setText('Data : ')
        self.lblStatus2.setText('저장할데이터 >')
        self.tblResult.setRowCount(0)
        self.btnNext.setEnabled(True)
    
    def tblResultSelected(self):
        selected = self.tblResult.currentRow() # 현재 선택된 열의 인덱스
        link = self.tblResult.item(selected,1).text()
        webbrowser.open(link)

    def btnSearchClikcked(self): # 슬롯(이벤트핸들러)
        jsonResult = []
        totalResult = []
        keyword = 'news'
        search_word = self.txtSearch.text()

        # QMessageBox(self, '결과', search_word)
        jsonResult = self.getNaverSearch(keyword,search_word,self.start,self.max_display)
        # print(jsonResult)
        for post in jsonResult['items']:
            totalResult.append(self.getPostData(post))
        # print(totalResult)
        self.makeTable(totalResult)

        # saveResult 값 할당, lblStatus /2 상태값을 표시
        total = jsonResult['total']
        curr = self.start+self.max_display-1

        self.lblStatus.setText(f'Data : {curr} / {total}')

        # saveResult 변수에 저장할 데이터 복사
        for post in totalResult:
            self.saveResult.append(post[0])

        self.lblStatus2.setText(f'저장할데이터 > {len(self.saveResult)} 개')

        if curr >=1000:
            self.btnNext.setDisabled(True)
        else:
            self.btnNext.setEnabled(True)
        return 

    def strip_tag(self,title): # html 태그를 없애주는 함수
        ret = title.replace('&lt;','<')
        ret = ret.replace('&gt;','>')
        ret = ret.replace('&qout;','"')
        ret = ret.replace('&apos;',"'")
        ret = ret.replace('&amp;','&')
        ret = ret.replace('<b>','')
        ret = ret.replace('</b>','')
        return ret
 
    def makeTable(self,result):
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(2)
        self.tblResult.setRowCount(len(result)) # displayCount에 따라서 변경
        self.tblResult.setHorizontalHeaderLabels(['기사제목','뉴스링크'])
        self.tblResult.setColumnWidth(0,350)
        self.tblResult.setColumnWidth(1,100)
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)

        i = 0
        for item in result:
            title = self.strip_tag(item[0]['title'])
            link = item[0]['originallink']
            self.tblResult.setItem(i,0,QTableWidgetItem(title))
            self.tblResult.setItem(i,1,QTableWidgetItem(link))
            i+=1

    def getPostData(self,post):
        temp = []
        title = self.strip_tag(post['title']) # 모든 곳에서 'title'의 html 태그 제거 
        description = post['description']
        originallink = post['originallink']
        link = post['link']
        pubDate = post['pubDate']

        temp.append({'title':title,
        'description':description,
        'originallink':originallink,
        'link':link,
        'pubDate':pubDate})
        return temp

    # 네이버 API 크롤링을 위한 함수
    def getNaverSearch(self,keyword,search_word,start,display):
        url = f'https://openapi.naver.com/v1/search/{keyword}.json'\
            f'?query={quote(search_word)}&start={start}&display={display}'
        req = urllib.request.Request(url)
        # 네이버 인증 추가
        req.add_header('X-Naver-Client-Id','ZXSDm8tUd9A5DceOnMb2')
        req.add_header('X-Naver-Client-Secret','PNbgyDA7G8')

        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            print('URL request success')
        else:
            prtin('url request failed')

        ret = res.read().decode('utf-8')
        if ret == None:
            return None     
        else:
            return json.loads(ret)

    def btn1_clicked(self):
        pass
        # self.label.setText('메시지 : btn01 버튼 클릭')
        # QMessageBox.critical(self,'signal','btn1_clicked') # 에러

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()