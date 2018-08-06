'''Usage:
  main.py path <path>


Options:
  -h --help     Show this screen.

'''
import urllib2
import pandas as pd
import requests
from bs4 import BeautifulSoup
from Suppliers import GearBest
import FileReaders.CSVFileReader
import re
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
    file_reader= FileReaders.CSVFileReader(arguments['path'])
    base = GearBest.Gearbest()
    var = base.do_scraping("https://www.gearbest.com/office-standing-desk/pp_641202.html?wid=1433363")
    print var


    res = requests.get("https://www.gearbest.com/office-standing-desk/pp_641202.html?wid=1433363")
    soup = BeautifulSoup(res.content, 'lxml')
    cost_text =  soup.text
    cost= re.findall(r"\d+\.\d+", cost_text)[0]





    tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")
    #tables = pd.read_html("https://apps.sandiego.gov/sdfiredispatch/")
    quote_page = "https://www.gearbest.com/rc-quadcopters/pp_568643.html?wid=1433363"
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, "html.parser")
    name_box = soup.find("h1", attrs = {"class":"price"})
    name = name_box.text.strip()  # strip() is used to remove starting
    print name