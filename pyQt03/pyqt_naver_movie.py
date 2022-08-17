import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from urllib.parse import quote
import urllib.request
import json
import webbrowser

# class OOP
class qTemplate(QWidget):

    # 생성자
    def __init__(self) -> None: # -> None 리턴 값이 없다 ( 생성자는 기본적으로 리턴값이 없음 ) Str : 문자열 반환 해야한다
        super().__init__()
        uic.loadUi('./pyQt02/naverMovie.ui',self)
        self.initUI()

    # 화면 정의를 위해서 만드 사용자 함수
    def initUI(self):
        self.addControls()
        self.show()

    def addControls(self):  # 위젯 정의, 이벤트(시그널) 처리
        self.btnSearch.clicked.connect(self.btnSearchClikcked)
        self.txtSearch.returnPressed.connect(self.btnSearchClikcked)
        self.tblResult.itemSelectionChanged.connect(self.tblResultSelected)

    def tblResultSelected(self):
        selected = self.tblResult.currentRow() # 현재 선택된 열의 인덱스
        link = self.tblResult.item(selected,2).text()
        webbrowser.open(link)

    def btnSearchClikcked(self): # 슬롯(이벤트핸들러)
        jsonResult = []
        totalResult = []
        keyword = 'movie'
        search_word = self.txtSearch.text()
        display_count = 50

        # QMessageBox(self, '결과', search_word)
        jsonResult = self.getNaverSearch(keyword,search_word,1,display_count)
        # print(jsonResult)
        for post in jsonResult['items']:
            totalResult.append(self.getPostData(post))
        # print(totalResult)
        self.makeTable(totalResult)
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
        self.tblResult.setColumnCount(3)
        self.tblResult.setRowCount(len(result)) # displayCount에 따라서 변경
        self.tblResult.setHorizontalHeaderLabels(['영화제목','상영년도','뉴스링크'])
        self.tblResult.setColumnWidth(0,350)
        self.tblResult.setColumnWidth(1,100)
        self.tblResult.setColumnWidth(2,100)
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)

        i = 0
        for item in result:
            title = self.strip_tag(item[0]['title'])
            subtitle = self.strip_tag(item[0]['subtitle'])
            pubDate = item[0]['pubDate']
            link = item[0]['link']
            self.tblResult.setItem(i,0,QTableWidgetItem(f'{title} / {subtitle}'))
            self.tblResult.setItem(i,1,QTableWidgetItem(pubDate))
            self.tblResult.setItem(i,2,QTableWidgetItem(link))
            i+=1

    def getPostData(self,post):
        temp = []
        title = post['title']
        subtitle = post['subtitle']
        link = post['link']
        pubDate = post['pubDate']

        temp.append({
            'title':title,
            'subtitle':subtitle,
            'link':link,
            'pubDate':pubDate
        })
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