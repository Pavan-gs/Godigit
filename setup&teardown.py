# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:34:15 2022

@author: Deepstrats
"""

# Setup --> Called before a method.
# Teardown --> Called after the method.

import unittest

class apptesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("This method is called before the execution of each methods")
    
    @classmethod  
    def tearDown(self):
        print("This method is called after the execution of each methods")
        
    def test_search(self):
        print("This is search test")
        
    def test_advancedsearch(self):
        print("this is advanced search test")
     
#unittest.__all__  
unittest.main()
        
if __name__ == '__main__':
    unittest.main()