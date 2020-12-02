from selenium import webdriver
import time
import json

driver = webdriver.Chrome(executable_path='/home/runner/work/Neworld_SignIn/Neworld_SignIn/driver/chromedriver')    # Chrome浏览器

# driver.deleted_all_cookies()

# driver.get('http://www.baidu.com') 
driver.get('https://neworld.date/user') 
#  获取cookies 
# time.sleep(10)
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

driver.refresh()#刷新页面 

driver.find_element_by_id("checkin").click() # 点击元素
