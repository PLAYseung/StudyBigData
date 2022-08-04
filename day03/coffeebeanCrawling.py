from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver

def getCoffeebeanInfo(result):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    wd = webdriver.Chrome('./day03/chromedriver.exe',options=options)

    for i in range(100,111):
        wd.get('https://www.coffeebeankorea.com/store/store.asp')
        time.sleep(1) #팝업 표시후 크롤링이 안되서 브라우저가 닫히는 것을 방지
        
        try:
            wd.execute_script(f"storePop2('{i}')")

            time.sleep(0.5) #팝업 표시후 크롤링이 안되서 브라우저가 닫히는 것을 방지

            html = wd.page_source
            soup = BeautifulSoup(html,'html.parser')
            store_name = soup.select('div.store_txt>h2')[0].string
            print(store_name)
            store_info = soup.select(('table.store_table > tbody > tr >td'))
            store_address_list = list(store_info[2])
            store_address = store_address_list[0].strip()
            store_contact_list = list(store_info[3])
            store_contact = store_contact_list[0].strip()
            result.append([store_name]+[store_contact]+[store_address])

        except Exception as e:
            print(e)
            continue

def main():
    result = []
    print('커피빈 매장 크롤링'+'>>'*10)
    getCoffeebeanInfo(result)

    columns = ['store','address','contact']
    dfCoffeebean = pd.DataFrame(result,columns=columns)

    dfCoffeebean.to_csv('./Coffeebean_shop_info.csv',index=True,encoding='utf-8')
    print('finish')

    del result[:]

if __name__=='__main__':
    main()