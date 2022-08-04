# 할리스 커피숍 매장 정보 크롤링
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def getHollysStoreInfo(result):
    for page in range(1,54):
        hollysUrl = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store='
        html = urllib.request.urlopen(hollysUrl)

        soup = BeautifulSoup(html,'html.parser')
        tbody = soup.find('tbody')
        
        for store in tbody.find_all('tr'):
            if len(store) <= 3: break

            store_td = store.find_all('td')

            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string

            result.append([store_name]+[store_sido]+[store_address]+[store_phone])

    # return result

def main():
    result = []
    print('할리스 매장 크롤링'+'>>'*10)
    getHollysStoreInfo(result)

    columns = ['store','sido-gu','address','phone']
    dfHollys = pd.DataFrame(result,columns=columns)

    dfHollys.to_csv('./Hollys_shop_info.csv',index=True,encoding='utf-8')
    print('finish')

    del result[:]

if __name__=='__main__':
    main()