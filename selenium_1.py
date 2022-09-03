# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:57:49 2022

@author: Deepstrats
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Edge(executable_path="C:\Drivers\edgedriver_win64\msedgedriver.exe")
driver.get("http://python.org")

#assert "Python" in driver.title

print(driver.title)
#driver.quit
driver.close()

