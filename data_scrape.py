from bs4 import BeautifulSoup
import requests 
import nltk 
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import matplotlib.pyplot as plt


def get_search_data(web_url):
    page = requests.get(web_url)
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

men_url = 'https://www.menshealth.com/search/?q=diet'
men_results = get_search_data(men_url)

women_url = 'https://www.womenshealthmag.com/search/?q=diet'
women_results = get_search_data(women_url)


men_diet_search = get_word_counts(men_results)
men_fd = nltk.FreqDist(men_diet_search)

women_diet_search = get_word_counts(women_results)
women_fd = nltk.FreqDist(women_diet_search)

men_fd.plot(10)
women_fd.plot(10)