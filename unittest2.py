# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:22:18 2022

@author: Deepstrats
"""

import unittest
from selenium import webdriver

class search_engine_test(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title of the page is ", + self.driver.title)
        
    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("Title of the page is ", + self.driver.title)
        
if __name__ =='__main__':
    unittest.main()