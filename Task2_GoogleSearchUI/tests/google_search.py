#Author: Ramiz Wahab

'''
Here i have automated a couple of test cases from Task2_TestCases.xls sheet
Since this is a pytest framework/solution, Execute this script from its root location 
Execution command: pytest -s -v google_search.py --html=<location of your directory>\..\GoogleSearchUI\report\htmlreport.html

Test Result:
TC1 = Fail (Deliberately failed to log result in report)
TC2 = Pass
TC3 = Pass

What i could have done better?
1. Optimizing the scripts, solution.
2. I have hard coded at multiple places, would make it more dynamic
3. Customize the html report to make it simpler with test case name and ids.

'''

#Import Packages
from selenium import webdriver
from pages.searchPage import SearchPage

import os
import unittest
import pytest

class GoogleSearchGUI(unittest.TestCase): #Suite
    
    #ChromeDriver Dependency
    driverLocation = "C:\\chromeDriver\\chromedriver.exe" #Provide path from your local machine
    os.environ["webdriver.chrome.driver"] = driverLocation
    driver = webdriver.Chrome(driverLocation)
    baseURL = "https://www.google.de/" #Web Address for AUT
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)
    
    @pytest.mark.run(order=3) #Order of execution is 3
    def test_search(self): #for a valid search
              
        spage = SearchPage(self.driver)
        spage.validSearch("microsoft")        
        self.driver.implicitly_wait(3)        
        result = spage.verifySuccessfulSearch()
        
        assert result == True
        spage.screenShot("ValidSearch")
                        
        self.driver.quit()
            
    @pytest.mark.run(order=2) #will be executed second
    def test_autodrop(self): #for checking auto drop suggestion
              
        spage = SearchPage(self.driver)
        spage.autoDrop("fac")        
        self.driver.implicitly_wait(3)        
        
        result = spage.verifyAutoDropdown()
        assert result == True        
        spage.screenShot("AutoDrop")
      
    @pytest.mark.run(order=1) #will be executed first
    def test_defaultLanguage(self): #For default language verification
        
              
        spage = SearchPage(self.driver)
        spage.getSearchBtn()        
        self.driver.implicitly_wait(3)        
        
        result = spage.verifyDefaultLang()
        spage.screenShot("Default Language") 
        assert result == True        
          
               