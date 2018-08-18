import Scraping
from Singleton import Singleton
import re

# @Singleton
class DX(Scraping.Scraping):

    @Scraping.catch_exceptions
    def do_scraping(self, url):
        result = super(DX,self).do_scraping(url,cookies={'DXGlobalization':'country=IL&lang=en&locale=he-IL&currency=USD','DXGlobalization_currency':'USD'})
        name_box = result.find( attrs={"class": "fl","id":"price"})

        return float(name_box.text)