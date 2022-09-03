# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 11:41:06 2022

@author: Deepstrats
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Edge(executable_path="C:\Drivers\edgedriver_win64\msedgedriver.exe")
driver.get("https://www.python.org/doc/")
#assert "Python" in driver.title
print(driver.title)
print(driver.current_url)
time.sleep(5)
#print(driver.page_source)
driver.find_element_by_xpath("//*[@id='touchnav-wrapper']/header/div/div[2]/div/p[3]/a").click()
driver.title
time.sleep(5)
#driver.quit
driver.close()

