from selenium import webdriver

driver = webdriver.Chrome('C:\chromedrver\chromedriver.exe')
driver.implicitly_wait(5)

driver.get('https://sports.news.naver.com/sports/new/live/index.nhn?category=worldfootball&gameId=2018100110014736365')

print("OK")