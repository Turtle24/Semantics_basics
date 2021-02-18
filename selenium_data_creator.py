from bs4 import BeautifulSoup
import requests 
import nltk 
from nltk.tokenize import word_tokenize, sent_tokenize
# from nltk.corpus import stopwords
import collections
import pandas as pd
import re
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())

class RetrieveSearchData:
    def __init__(self, name, search):
        self.name = name
        self.search = search
        
    # Search data method
    def get_search_data(self, scrolling=True):
        # Selenium
        websites = {'men': 'https://www.menshealth.com/search/?q=', 'women': 'https://www.womenshealthmag.com/search/?q='}
        web_url = websites[self.name] + self.search
        driver.get(web_url)
        time.sleep(3)
        button = driver.find_element_by_id("onetrust-accept-btn-handler")
        button.click()
        count = 0
        while scrolling:
            count += 1
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
            wait = WebDriverWait(driver,10)
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))
                element.click()
                print(f"Page/s: {count}")
            except:
                print("Done")
                scrolling = False
            
        # Soup
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        results = soup.find(class_='feed feed-grid')
        job_elems = results.find_all('div', class_='simple-item-title item-title')
        return job_elems
        
    # Search term word count in titles
    def get_word_counts(self, elem_jobs):
        c = collections.Counter()
        for elem_job in elem_jobs:
            text = elem_job.text
            words = nltk.tokenize.word_tokenize(text)
            words_tag = nltk.pos_tag(words)
            words_select = [word for word, pos in words_tag if pos.startswith("NNP") or pos.startswith('VB')]
            c.update(words_select) 
        return c.most_common(10)   #nltk.FreqDist(all_words)

    def create_csv(gender, search_term):
        search = RetrieveSearchData(gender, search_term)
        search_data = search.get_search_data()
        search_results = search.get_word_counts(search_data)
        return pd.DataFrame(search_results, columns=['word', 'count']).to_csv('data/'+ gender + '_' + search_term +'.csv', index=False)

RetrieveSearchData.create_csv('women', 'diet')