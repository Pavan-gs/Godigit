# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 10:26:52 2022

@author: Deepstrats
"""

'''is_enabled, is_displayed,is_selected'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Edge(executable_path="C:\Drivers\edgedriver_win64\msedgedriver.exe")

driver.get("https://demo.guru99.com/test/newtours/")
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
time.sleep(3)
driver.find_element("xpath","/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a").click()
time.sleep(3)
radio_roundtrip=driver.find_element_by_css_selector("input[value=roundtrip]")
print("The status of selection for roundtrip is: ",radio_roundtrip.is_selected())
driver.close()

