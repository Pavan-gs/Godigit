# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 16:10:17 2022

@author: Deepstrats
"""
# scroll through different elements


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# scroll down using pixels
#driver.execute_script("window.scrollBy(0,2000)","")
# Scroll till the item is found
#flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();",flag)
#driver.execute_script()
# Scroll till the end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")