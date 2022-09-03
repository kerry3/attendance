from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

driver = webdriver.Chrome('chromedriver', chrome_options=options)
url='https://opga101.com/bbs/login.php' #들어가려는 사이트 주소

#1.26 web driver 버전 바뀌어서 다시 깔아줌. 코드랑 같은 폴더에 있게 하자.

driver.get(url)  #사이트 접속

driver.find_element_by_id('login_id').send_keys('mynamehaha') #id로 찾음, 개발자 도구로 login_id가지고 있다는거 알아내고 그거로 접근. send_key로 아이디 myname haha를 쏴줌 
driver.find_element_by_id('login_pw').send_keys('123123')

driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div/div/div[2]/div[1]/div/div/form/button').click() # 로그인 버튼 클릭. xpath로 접근. 버튼에 우클릭 하고 xpath 찾기 하면됨. click함수로 클릭시킴.
#1.26 이거 element값 바뀌어서 다시 xpath따서 변경해줌


driver.find_element_by_xpath('//*[@id="undefined-sticky-wrapper"]/nav/div[1]/div[1]/div/div/ul/li[7]/a').click() # 커뮤니티 버튼 누르기. 바로 출석체크 창으로 뜸.

driver.find_element_by_xpath('//*[@id="talk_submit"]').click() # 출석체크 버튼 누르기
