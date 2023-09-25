# _*_ coding: UTF-8 _*_
#pip freeze > d:/requirements.txt
#pip install -r requirement.txt

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
# 不显示浏览器
# options.add_argument("--headless")
# 执行完后不自动关闭浏览器
options.add_experimental_option('detach',True)
# 如何去掉提示“正受到自动测试软件控制”
options.add_experimental_option("excludeSwitches", ['enable-automation']);

driver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
service = Service(executable_path=driver_path)

driver = webdriver.Chrome(options=options)
driver.get("https://www.baidu.com")
time.sleep(2)
# 浏览器窗口最大化
driver.maximize_window()
el = driver.find_element(By.ID,"xxx")
el.click()
el = driver.find_element(By.ID,"xxxxx")
el.send_keys("xxxx")

# driver.switch_to.window(driver.window_handles[-1])#定位到最新打开窗口

driver.switch_to.frame("iframe1")
el = driver.find_element(By.ID,"xxx")
el.send_keys("xxx")
# driver.switch_to.default_content()

iframe2 = driver.find_element(By.XPATH,"/html/body/iframe[3]")
driver.switch_to.frame(iframe2)
el = driver.find_element(By.ID,"xxx")
el.click()
# #切换到iframe
# driver.switch_to.frame("xxx")
#
# #定位到子iframe
# driver.switch_to.frame("xxx")
# driver.switch_to.default_content() #返回主页面
# #切换到父iframe
# driver.switch_to.parent_frame()

# el = driver.find_element(By.ID,'xxx')
# value = el.get_attribute("")
# print(value)
# 通过 find_element_by_id() 方法获取文本框对象，再使用 get_attribute() 方法获取文本框的值
