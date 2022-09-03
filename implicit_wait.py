# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 11:40:53 2022

@author: Deepstrats
"""

''' implicit wait, explicit wait '''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Edge(executable_path="C:\Drivers\edgedriver_win64\msedgedriver.exe")

driver.get("https://demo.guru99.com/test/newtours/")
driver.implicitly_wait(10)
assert "Welcome: Mercury Tours" in driver.title
print(driver.title)
#time.sleep(5)
user_ele = driver.find_element_by_name("userName").send_keys("mercury")
#user_ele = driver.find_element("name","userName")
#print(user_ele.is_displayed())
#print(user_ele.is_enabled())
pass_ele = driver.find_element_by_name("password").send_keys("mercury123")
#print(pass_ele.is_displayed())
#print(pass_ele.is_enabled())
driver.find_element("name","submit").click()