# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:53:44 2019

@author: boy19
"""

"""
Selenium will be used to help extract requirement section

Since selenium is used, a chrome windown will pop up shortly after running the program
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

class WebBrowserController:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\boy19\Desktop\chromedriver_win32\chromedriver.exe')
        self.indeed = 'https://www.indeed.com'
        self.urlList = []
        
    def getRequirementHtml(self, requirementUrl):
        self.driver.get(requirementUrl);
        soup = BeautifulSoup(self.driver.page_source)
        [s.extract() for s in soup('script')] 
        return str(soup.find_all(text = True))
        
    def getAllPostingURL(self, title, location):
        self.indeedSearch(title, location)
        source = self.driver.page_source
        soup = BeautifulSoup(source, 'html.parser')
        for jobCard in soup.find_all('div', class_ = 'jobsearch-SerpJobCard unifiedRow row result clickcard'):
            for title in jobCard.find_all('div', class_ = 'title'):
                for url in title.find_all('a'):     
                    #append www.indeed.com to url to get full URL
                    self.urlList.append(self.indeed + str(url['href']))                    
            
        
    #input and search
    def indeedSearch(self, title, location):
        self.driver.get(self.indeed)
        titleInput = self.driver.find_element_by_id('text-input-what')
        titleInput.send_keys(Keys.CONTROL + "a");
        titleInput.send_keys(title)
        
        #indeed have auto input on the location field, hence control + a to select existing input before replacing with our input
        LocationInput = self.driver.find_element_by_id('text-input-where')
        LocationInput.send_keys(Keys.CONTROL + "a");
        LocationInput.send_keys(location)
        
        #close the suggested words, and search
        LocationInput.send_keys(Keys.ENTER)
        LocationInput.send_keys(Keys.ENTER)
        
        