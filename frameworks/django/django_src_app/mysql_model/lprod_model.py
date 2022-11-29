import pymysql

### Database connection 및 cursor 객체 생성하기
def getConnection() :
    host = "localhost"
    port = 3306
    database = "django_src"
    username = "django"
    password = "dbdb"

    ### MySQL 서버에 접속하기
    conn = pymysql.connect(host=host, 
                        user=username, 
                        passwd=password, 
                        db=database, 
                        port=port, 
                        use_unicode=True, 
                        charset='utf8')
    
    ### 서버로부터 Cursor 받아오기
    cursor = conn.cursor()
    
    return conn, cursor


### 컬럼명 추출하기
def getColumns(colname) :
    cols = []
    for col in colname :
        cols.append(col[0])    
    return cols


### 여러건 조회결과 리스트+딕셔너리 형태로 생성하기
def getList_DictType_FetchAll(cols, rows) :
    list_rows = []
    for columns in rows :
        dict_row = {}

        for i in range(0, len(columns), 1) :
            # 위에 조회된 컬럼명은 대문자로 처리되기 때문에 소문자로 변환하여 사용..
            dict_row[cols[i].lower()] = columns[i]

        list_rows.append(dict_row)
        
    return list_rows


### 딕셔너리로 데이터 구성하기..
def getDictType_FetchOne(cols, one_row) :
    dict_row = {}    
    for i in range(0, len(one_row), 1) :
        # 조회된 컬럼명은 대문자로 처리되기 때문에 소문자로 변환하여 사용..
        dict_row[cols[i].lower()] = one_row[i]
        
    ### 결과
    return dict_row


# cursor 및 conn 객체 반환, DB와의 연결을 끊어준다
def dbClose(cursor, conn) :
    # 커서 반납하기
    cursor.close()
    
    # DB와의 접속 끊기
    conn.close()
    

### lprod 테이블 [전체 조회]하기
def getLprodList() :
    ### Database connection 및 cursor 객체 받아오기
    conn, cursor = getConnection()
    
    ### 조회하기
    sql = """
        Select *
        From lprod
    """
    
    ### sql 실행하기
    cursor.execute(sql)
    
    ### 실행 결과 가지고 오기
    rows = cursor.fetchall()
    
    ### 컬럼명 추출하기
    cols = getColumns(cursor.description)
    
    ### MySQL 객체 반납하기
    dbClose(cursor, conn)
    
    ### [여러건 조회인 경우] 리스트 + 딕셔너리 형태로 만들기
    list_rows = getList_DictType_FetchAll(cols, rows)
    
    return list_rows    
    
### lprod 테이블 [상세 조회]하기
def getLprodView(p_lprod_gu) :
    ### Database connection 및 cursor 객체 받아오기
    conn, cursor = getConnection()
    
    ### 조회하기
    sql = """
        Select *
        From lprod
        Where lprod_gu = %s
    """
    
    ### sql 실행하기
    params = (p_lprod_gu, )
    cursor.execute(sql, params)
    
    ### 실행 결과 가지고 오기
    one_row = cursor.fetchone()
    
    ### 컬럼명 추출하기
    cols = getColumns(cursor.description)
    
    ### MySQL 객체 반납하기
    dbClose(cursor, conn)
    
    ### [한건 조회인 경우] 딕셔너리 형태로 만들기
    dict_row = getDictType_FetchOne(cols, one_row)
    
    return dict_row


### lprod 테이블 [입력]하기
def setLprodInsert(p_params) :
    ### Database connection 및 cursor 객체 받아오기
    conn, cursor = getConnection()
    
    ### 조회하기
    sql = """
        Insert Into lprod (lprod_id, lprod_gu, lprod_nm ) 
        Values (%s, %s, %s)
    """
    
    ### sql 실행하기
    params = (p_params["lprod_id"], p_params["lprod_gu"], p_params["lprod_nm"])
    cursor.execute(sql, params)
    
    ### 데이터 변경 영구 반영하기 
    conn.commit()
    
    ### MySQL 객체 반납하기
    dbClose(cursor, conn)
    
    return "ok"


### lprod 테이블 [수정]하기
def setLprodUpdate(p_params) :
    ### Database connection 및 cursor 객체 받아오기
    conn, cursor = getConnection()
    
    ### 조회하기
    sql = """
        Update lprod
        Set lprod_nm = %s
        Where lprod_gu = %s
    """
    
    ### sql 실행하기
    params = (p_params["lprod_nm"], p_params["lprod_gu"])
    cursor.execute(sql, params)
    
    ### 데이터 변경 영구 반영하기 
    conn.commit()
    
    ### MySQL 객체 반납하기
    dbClose(cursor, conn)
    
    return "ok"


### lprod 테이블 [삭제]하기
def setLprodDelete(p_lprod_gu) :
    ### Database connection 및 cursor 객체 받아오기
    conn, cursor = getConnection()
    
    ### 조회하기
    sql = """
        Delete From lprod
        Where lprod_gu = %s
    """
    
    ### sql 실행하기
    params = (p_lprod_gu, )
    cursor.execute(sql, params)
    
    ### 데이터 변경 영구 반영하기 
    conn.commit()
    
    ### MySQL 객체 반납하기
    dbClose(cursor, conn)
    
    return "ok"