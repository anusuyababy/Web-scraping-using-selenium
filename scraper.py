# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 16:26:05 2021

@author: DELL
"""

#importing all necessary libraries
from selenium import webdriver
from selenium.common import exceptions
import pandas as pd

browser = webdriver.Chrome('chromedriver.exe')

#preprocessing and scraping the data from the website through for loop
element_list = []
for page in range(1, 25, 1):
    # giving url of the walmart
    browser.get('https://www.walmart.com/reviews/product/14898365?sort=submission-desc&page=' + str(page))
    
    date = browser.find_elements_by_xpath('//span[@class="review-date-submissionTime"]')
    reviewer = browser.find_elements_by_xpath('//span[@class="review-footer-userNickname"]')
    title = browser.find_elements_by_xpath('//h3[@class="review-title font-bold"]')
    review = browser.find_elements_by_xpath('//div[@class="review-text"]')
    rating = browser.find_elements_by_xpath('//span[@class="visuallyhidden seo-avg-rating"]')
    
    
    for i in range(len(title)):
        element_list.append([date[i].text, reviewer[i].text, title[i].text, review[i].text, rating[i].text])
        
print(element_list)

# creating dataframe for that data
df = pd.DataFrame(element_list, columns=['Date', 'Reviewer Name', 'Title', 'Review', 'Rating'])
df.head()

df.shape

df.to_csv('output.csv', index=False)
browser.close()