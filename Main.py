'''Usage:
  main.py path <path> timer <timer>


Options:
  -h --help     Show this screen.
  <timer> timer to sleep in minuets

'''

from Suppliers import GearBest, DX
from FileReaders.CSVFileReader import CSVFileReader
from docopt import docopt
import Loger
import time




import win32serviceutil
import win32service
import win32event
import servicemanager
import socket

def load_config():
    from ConfigParser import SafeConfigParser
    parser = SafeConfigParser()
    parser.read(r'C:\Users\vladi\PycharmProjects\PriceTracker\config.ini')
    result = (parser.get('initialize', 'svc_path'),parser.get('initialize', 'time_out_in_min'))
    print result
    return result

def main_func(path):
    Loger.logger.info('The price tracker was started')
    # define the suppliers dictionary when the key is the supplier name
    suppliers = {'gearbest': GearBest.Gearbest(), 'dx': DX.DX()}

    #arguments = docopt(__doc__)
    # initialize the csv reader with path from command line argument
    file_reader = CSVFileReader(path)#(arguments['<path>'])

        # read the csv file
    lists = file_reader.read()
    for list in lists:  # iterate the all item
        updated_price = suppliers[list.supplier.lower()].do_scraping(
            list.url)  # get actual price of item from the site
        if updated_price <> float(list.price):
            Loger.logger.warn('The url {} price has been changed from {} to {}'.format(list.ebay_url, list.price,
                                                                                           updated_price))  # to do somthing

    Loger.logger.info('The price tracker was finished')









class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "PriceTracker"
    _svc_display_name_ = "Price Tracker for Listings"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)
        self.isAlive = True

    def SvcStop(self):
        self.isAlive = False
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        self.isAlive = True
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        self.main()
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    def main(self):
        while self.isAlive:
            path, time_out = load_config()
            main_func(path)
            time.sleep(float(time_out)*60)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)





















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