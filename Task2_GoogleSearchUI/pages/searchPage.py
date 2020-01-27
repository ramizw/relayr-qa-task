from selenium.webdriver.common.by import By
import time
import os

class SearchPage():
    
    def __init__(self, driver):
        self.driver = driver
    
    #######################################
    #Locators
    #######################################
    _search_field = '//input[@name="q"]'
    _search_btn = '//input[@name="btnK"]'
    
    
    #######################################
    #Element Interaction
    #######################################
    
    #Element Search
    def getSearchField(self):
        return self.driver.find_element_by_xpath(self._search_field)
    
    def getSearchBtn(self):
        return self.driver.find_element_by_xpath(self._search_btn)
    
    
    
    #Action performed on elements
    def enterSearchText(self, searchE):
        self.getSearchField().clear()
        self.getSearchField().send_keys(searchE)
    
    def clickSearchBtn(self):
        self.getSearchBtn().click()
        
    def validSearch(self, searchE):
        self.enterSearchText(searchE)
        self.clickSearchBtn()  
        
    def autoDrop(self, searchE):
        self.enterSearchText(searchE)        
    
       
    #Validation
       
    def verifyDefaultLang(self):
        element = self.driver.find_element_by_xpath('//input[@name="btnK"]')
        lang = element.get_attribute('aria-label')
        
        if "Google-Suche" in lang: #checks if default language is Deutsch
            return True
        else:
            return False
    
    
    def verifySuccessfulSearch(self): #Verification of valid Search
        searchResult = self.driver.find_element_by_xpath('//a[@href="https://www.microsoft.com/en-in"]')
        if searchResult is not None:
            return True
        else:
            return False
        
    def verifyAutoDropdown(self): #Verification of Auto Dropdown
        autoDrop = self.driver.find_element_by_xpath('//ul[@class="erkvQe"]')
        if autoDrop is not None:
            return True
            
        else:
            return False
    
    #To take screenshot of current open web page
    def screenShot(self, testName):        
        fileName = testName + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        
        if not os.path.exists(destinationDirectory):
            os.makedirs(destinationDirectory)
        self.driver.save_screenshot(destinationFile)
            
        
                    