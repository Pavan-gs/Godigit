# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 12:22:41 2022

@author: Deepstrats
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Edge(executable_path="C:\Drivers\edgedriver_win64\msedgedriver.exe")
driver.get("http://python.org")
#assert "Python" in driver.title
print(driver.title)
#print(driver.current_url)
#print(driver.page_source)

time.sleep(10)

driver.get("https://www.python.org/blogs/")
print(driver.title)

time.sleep(5)

driver.back()

print(driver.title)
time.sleep(5)

driver.forward()
print(driver.title)

#driver.quit
driver.close()
