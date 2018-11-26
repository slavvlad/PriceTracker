import Scraping
import re


class Tmart(Scraping.Scraping):

    @Scraping.catch_exceptions
    def do_scraping(self, url):
        result = super(Tmart,self).do_scraping(url, cookies={'currency': 'USD'})
        name_box = result.find(attrs={"class": "font36 strong font-light-red"})
        #text= result.text.lstrip().splitlines()[0]
        return float(re.findall(r"\d+\.\d+", name_box.text)[0])

    def is_in_stock(self,url):
        pass