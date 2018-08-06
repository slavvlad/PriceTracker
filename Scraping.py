import abc
import urllib2
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


class Scraping:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def do_scraping(self, url):
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'lxml')
        return soup
