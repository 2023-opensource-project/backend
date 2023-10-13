from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

driver = webdriver.Chrome()
driver.implicitly_wait(15) # 화면이 켜질때까지 최대 15초 기다린다.
driver.get('https://www.naver.com')
driver.maximize_window()
while(True):
    try:
        driver.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW').click()
        #time.sleep(3)
        nid = 'swmsc'
        pyperclip.copy(nid)
        driver.find_element(By.CSS_SELECTOR, '#id').send_keys(Keys.CONTROL+'v')
        #time.sleep(1)
        npw = 'hlove330812@'
        pyperclip.copy(npw)
        secure = 'blank'
        driver.find_element(By.CSS_SELECTOR, '#pw').send_keys(Keys.CONTROL + 'v')
        pyperclip.copy(secure)
        driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
        driver.get('https://cafe.naver.com/dokchi')
        driver.find_element(By.CLASS_NAME, 'gm-tcol-c b').click()
        driver.get('https://cafe.naver.com/dokchi?iframe_url=/ArticleList.nhn%3Fsearch.clubid=16996348%26search.menuid=1178%26search.boardtype=L')

    except:
        print("no such element")