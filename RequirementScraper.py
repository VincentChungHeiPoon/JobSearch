# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:03:11 2019

@author: Vincent Poon

This file contains all functions needed to scrap the following list of website:
    
It will return text from the website for further processing
"""

from bs4 import BeautifulSoup
import requests
import WebBrowserController

'''
indeed.com
The scraped link did not 'click' on any tab.
Causing targeted elements not shown in HTML
'''
