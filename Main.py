'''Usage:
  main.py path <path>


Options:
  -h --help     Show this screen.

'''

from Suppliers import GearBest
from FileReaders.CSVFileReader import CSVFileReader
from docopt import docopt

if __name__ == '__main__':
    suppliers ={'gearbest': GearBest.Gearbest()}
    arguments = docopt(__doc__)
    file_reader= CSVFileReader(arguments['<path>'])
    lists = file_reader.read()
    for list in lists:
        updated_price = suppliers[list.supplier.lower()].do_scraping(list.url)
        if updated_price>float(list.price):
            print "problem"
    # base = GearBest.Gearbest()
    # var = base.do_scraping("https://www.gearbest.com/office-standing-desk/pp_641202.html?wid=1433363")
    # print var
    #
    #
    # res = requests.get("https://www.gearbest.com/office-standing-desk/pp_641202.html?wid=1433363")
    # soup = BeautifulSoup(res.content, 'lxml')
    # cost_text =  soup.text
    # cost= re.findall(r"\d+\.\d+", cost_text)[0]
    #
    #
    #
    #
    #
    # tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")
    # #tables = pd.read_html("https://apps.sandiego.gov/sdfiredispatch/")
    # quote_page = "https://www.gearbest.com/rc-quadcopters/pp_568643.html?wid=1433363"
    # page = urllib2.urlopen(quote_page)
    # soup = BeautifulSoup(page, "html.parser")
    # name_box = soup.find("h1", attrs = {"class":"price"})
    # name = name_box.text.strip()  # strip() is used to remove starting
    # print name