'''Usage:
  main.py path <path> timer <timer>


Options:
  -h --help     Show this screen.
  <timer> timer to sleep in minuets

'''

from Suppliers import GearBest
from FileReaders.CSVFileReader import CSVFileReader
from docopt import docopt
import Loger
import time

if __name__ == '__main__':
    #define the suppliers dictionary when the key is the supplier name
    suppliers ={'gearbest': GearBest.Gearbest()}
    arguments = docopt(__doc__)
    #initialize the csv reader with path from command line argument
    file_reader= CSVFileReader(arguments['<path>'])
    while True:
        #read the csv file
        lists = file_reader.read()
        for list in lists:# iterate the all item
            updated_price = suppliers[list.supplier.lower()].do_scraping(list.url)#get actual price of item from the site
            if updated_price>float(list.price):
                Loger.logger.warn('The url {} price has been changed from {} to {}'.format(list.url,list.price,updated_price))# to do somthing
        time.sleep(float(arguments['<timer>']))














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