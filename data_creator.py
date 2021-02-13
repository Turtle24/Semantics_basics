from bs4 import BeautifulSoup
import requests 
import nltk 
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import matplotlib.pyplot as plt

class RetrieveSearchData:
    def __init__(self, name, search):
        self.name = name
        self.search = search
        
    # Search data method
    def get_search_data(self):
        websites = {'men': 'https://www.menshealth.com/search/?q=', 'women': 'https://www.womenshealthmag.com/search/?q='}
        web_url = websites[self.name] + self.search
        page = requests.get(web_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(class_='feed feed-grid')
        job_elems = results.find_all('div', class_='simple-item-title item-title')
        return job_elems

    # Search term word count in titles
    def get_word_counts(self, elem_jobs):
        all_words = []
        for elem_job in elem_jobs:
            text = elem_job.text
            words = nltk.tokenize.word_tokenize(text)
            all_words += words
        return nltk.FreqDist(all_words)
