# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 20:46:14 2022

@author: Deepstrats
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Edge(executable_path="C:\Drivers\edgedriver_win64\msedgedriver.exe")
driver.get("https://demo.guru99.com/test/newtours/")
#assert "Python" in driver.title
print(driver.title)
#print(driver.current_url)
time.sleep(5)
user_ele = driver.find_element_by_name("userName")

print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())
#print(driver.page_source)
#driver.quit

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury123")

driver.find_element_by_name("submit").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a").click()
roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print("status of round trip selection", roundtrip_radio.is_selected())

driver.close()  