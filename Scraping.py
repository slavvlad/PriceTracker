import abc
import urllib2
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


class Scraping:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def do_scraping(self, url,cookies=None):
        res = requests.get(url,cookies=cookies)
        soup = BeautifulSoup(res.content, 'lxml')
        #print(soup.prettify())
        return soup
