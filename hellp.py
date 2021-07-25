from selenium import webdriver
import time
import json
import os
from selenium.webdriver.chrome.options import Options


# 虚拟出Chrome界面
chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# action  linux服务器驱动地址
driver = webdriver.Chrome(executable_path='/home/runner/work/Neworld_SignIn/Neworld_SignIn/driver/chromedriver',chrome_options=chrome_options)    # Chrome浏览器  
# driver = webdriver.Chrome(executable_path='/home/runner/work/Neworld_SignIn/Neworld_SignIn/driver/chromedriver')    # Chrome浏览器  

# windows 系统驱动路径
# driver = webdriver.Chrome(executable_path='D:\Downloads\chromedriver_win32\chromedriver.exe')    # Chrome浏览器

driver.get('https://neworld.tv/auth/login') 

u = os.environ["USERNAME"]
p = os.environ["PASSWORD"]
print('u',u)
print('p',p)
#  获取cookies 
time.sleep(5)
# 账号密码登录版本
driver.find_element_by_id('email').clear()
driver.find_element_by_id("email").send_keys(u)

driver.find_element_by_id('passwd').clear()
driver.find_element_by_id("passwd").send_keys(p)

time.sleep(1)
driver.find_element_by_id("login").click()

driver.refresh()#刷新页面 

# cookies版本
# cookies = driver.get_cookies()
# print (type(cookies))
# # print ("".join(cookies))
# f1 = open('cookie.txt', 'w')
# f1.write(json.dumps(cookies))

# f1 = open('cookie.txt')
# cookie = f1.read()
# cookie =json.loads(cookie)
# for c in cookie:
#     driver.add_cookie(c)

driver.refresh()#刷新页面 

# time.sleep(5)

# buttons = driver.find_element_by_xpath("//button[@id='checkin']")
# print('buttons',buttons)

driver.find_element_by_id("checkin").click() # 点击元素
