from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

driver = webdriver.Chrome('chromedriver', chrome_options=options)
url='https://opga100.com/bbs/login.php' #들어가려는 사이트 주소

#1.26 web driver 버전 바뀌어서 다시 깔아줌. 코드랑 같은 폴더에 있게 하자.

driver.get(url)  #사이트 접속

print(driver.page_source)

#headless 로해도 똑같음.
