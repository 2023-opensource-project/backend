from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

driver = webdriver.Chrome()
driver.implicitly_wait(15) # 화면이 켜질때까지 최대 15초 기다린다.
driver.get('https://www.naver.com')
driver.maximize_window()
driver.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW').click()
nid = 'swmsc'
pyperclip.copy(nid)
driver.find_element(By.CSS_SELECTOR, '#id').send_keys(Keys.CONTROL+'v')
npw = 'hlove330812@'
pyperclip.copy(npw)
secure = 'blank'
driver.find_element(By.CSS_SELECTOR, '#pw').send_keys(Keys.CONTROL + 'v')
pyperclip.copy(secure)
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
# 여기까지 로그인
driver.get('https://cafe.naver.com/dokchi/ArticleList.nhn?search.clubid=16996348&search.menuid=1178&search.boardtype=L')
bb2 = []
dataset = []
time.sleep(2)
driver.switch_to.frame("cafe_main")
time.sleep(2)
# driver.find_elements(By.XPATH, '//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div')
# driver.find_elements(By.CSS_SELECTOR, 'a').click()
for l in range(1,2):
    tag = driver.find_elements(By.XPATH,'//div[@class="article-board m-tcol-c"]//table/tbody/tr')
    bb2 = tag
    time.sleep(2)
    for i in range(len(bb2)):
        dataset.append(bb2[i].text)
    if l % 10 == 0:
        c10 = driver.find_element(By.LINK_TEXT,'다음')
        c10.click()
    else:
        a = str(l+1)
        c = driver.find_element(By.LINK_TEXT,a)
        c.click()
    time.sleep(2)
driver.quit()
print(dataset)
#driver.find_element(By.XPATH, '//*[@id="menuLink1178"]').click()
#driver.find_element(By.XPATH, '//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()
#driver.find_element(By.CLASS_NAME, 'gm-tcol-c b').click()
#driver.get('https://cafe.naver.com/dokchi?iframe_url=/ArticleList.nhn%3Fsearch.clubid=16996348%26search.menuid=1178%26search.boardtype=L')