import abc
import requests
from bs4 import BeautifulSoup


def catch_exceptions(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return -1

    return func_wrapper

class Scraping:
    __metaclass__ = abc.ABCMeta



    @abc.abstractmethod
    # @try_decorate
    def do_scraping(self, url,cookies=None):
        res = requests.get(url,cookies=cookies)
        soup = BeautifulSoup(res.content, 'lxml')
        #print(soup.prettify())
        return soup

