# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:07:37 2019

@author: boy19

Main.py is used to execute the program.
"""

from seleniumAutoUser import WebBrowserController
from TextProcessing import KeyWord
from TextProcessing import keyWordFilter
  
class Scraper:
    def __init__(self):
        self.controller = WebBrowserController()
        self.keyWordFilter = keyWordFilter()
        
    def getJobSkillsFor(self, title, location):
        self.controller.getAllPostingURL(title, location)
        for url in self.controller.urlList:
            requirement = self.controller.getRequirementHtml(url)
            keyWordList = self.keyWordFilter.filterTagAndSelectTokens(requirement)
            for word in keyWordList:
                self.keyWordFilter.addWordToList(word)
        
a = Scraper()
a.getJobSkillsFor('software developer', 'houston')
print(a.keyWordFilter.printKeyWord(5))