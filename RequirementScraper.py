# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:03:11 2019

@author: Vincent Poon

This file contains all functions needed to scrap the following list of website:
    
It will return text from the website for further processing
"""

from bs4 import BeautifulSoup
import requests


url = "https://www.indeed.com/jobs?q=software%20developer&l=Houston%2C%20TX&oq=software%20developer%20%2490%2C000%1Fsoftware%20developer&ol=Houston%2C%20TX%1FHouston%2C%20TX&ts=1563488118807&pts=1563231640432&rq=1&fromage=last&advn=122089296871042&vjk=83e3314be5a6cc70"
result = requests.get(url)

soup = BeautifulSoup(result.text, 'lxml')
#print(soup.prettify())
#print(soup.find_all('table', id = 'pageContent'))
#print(soup.find_all('td', id = 'auxCol'))
print(soup.find_all('div', id = 'vjs-header'))
print(soup.find_all('p'))

'''
indeed.com
The scraped link did not 'click' on any tab.
Causing targeted elements not shown in HTML
'''