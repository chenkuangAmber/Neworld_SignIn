from selenium import webdriver
import time
import json

from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path='/home/runner/work/Neworld_SignIn/Neworld_SignIn/driver/chromedriver',chrome_options=chrome_options)    # Chrome浏览器

# driver.deleted_all_cookies()

# driver.get('http://www.baidu.com') 
driver.get('https://neworld.date/user') 
#  获取cookies 
time.sleep(5)
# cookies = driver.get_cookies()
# print (type(cookies))
# # print ("".join(cookies))
# f1 = open('cookie.txt', 'w')
# f1.write(json.dumps(cookies))

f1 = open('cookie.txt')
cookie = f1.read()
cookie =json.loads(cookie)
for c in cookie:
    driver.add_cookie(c)
    print('cookies',c)

driver.refresh()#刷新页面 

time.sleep(5)
driver.find_element_by_id("checkin").click() # 点击元素
