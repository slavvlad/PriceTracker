import abc
import requests
from bs4 import BeautifulSoup

# To get relevant cookies from supplier site make following:
# click F12
# Choose 'Network' in the header of console, when the first row in left panel and 'Headers' in header of right panel
# Scrool down to 'Request Headers' and see 'Cookie' field

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

