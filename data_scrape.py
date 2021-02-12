from bs4 import BeautifulSoup
import requests 
import nltk 
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import matplotlib.pyplot as plt


def get_search_data(web_url):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_='feed feed-grid')
    job_elems = results.find_all('div', class_='simple-item-title item-title')
    return job_elems

def get_word_counts(elem_jobs):
    all_words = []
    for elem_job in elem_jobs:
        text = elem_job.text
        words = nltk.tokenize.word_tokenize(text)
        all_words += words
    return all_words
    
URL = 'https://www.menshealth.com/search/?q=diet'
results = get_search_data(URL)

diet_search = get_word_counts(results)

fd = nltk.FreqDist(diet_search)

fd.plot(10)