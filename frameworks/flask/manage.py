########################################
### 필수 - flask 기본 패키지
from flask import Flask

### 필수 - flask 시작점 
app = Flask(__name__)


########### 아래에 프로그램 작성 ##############

### index 페이지
@app.route('/')
def index() :
	# return 'Index 페이지 입니다.'
	# templates 폴더 내에 html 파일 지정하기
	return render_template("/index.html")


############ [Lprod(상품분류) 데이터 관리] #############

# flask에서 templates 폴더 사용하기
from flask import render_template

# flask에서 GET / POPST 파라메터 받아오는 패키지
from flask import request

# static 폴더 사용하기
from flask import url_for

# lprod 테이블 데이터 처리
from models import lprod

### lpord 테이블 [전체 조회]
@app.route('/lprodList/')
def lprodList() :
	data = lprod.getLprodList()

	# templates 폴더 내에 html 파일 지정하기
	return render_template("/lprod/lprodList.html",
							list_rows = data)

### lpord 테이블 [상세 조회]
@app.route('/lprodView/', methods=['POST'])
def lprodView() :
	# 파라메터 받아오기
	p_lprod_gu = request.form["lprod_gu"]
	data = lprod.getLprodView(p_lprod_gu)

	# templates 폴더 내에 html 파일 지정하기
	return render_template("/lprod/lprodView.html",
							dict_row = data)

### static 폴더를 이용한 이미지 처리
@app.route('/viewStaticImg/')
def viewStaticImg() :
	### 이미지
	p_img_path = "images/dog.jpg"

	# templates 폴더 내에 html 파일 지정하기
	return render_template("/imgView/viewStaticImg.html",
							img_path = p_img_path)


########################################
### 필수 - flask 시작 옵션 - 하단에 작성
if __name__ == '__main__':
    # debug=True는 코드 수정 후 웹브라우저 새로고침 시 반영되게.
	app.run(debug=True)