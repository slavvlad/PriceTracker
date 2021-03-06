'''Usage:
  main.py path <path> timer <timer>


Options:
  -h --help     Show this screen.
  <timer> timer to sleep in minuets

'''
from EbaySource import Ebay
from Suppliers import GearBest, DX, TMart
from FileReaders.CSVFileReader import CSVFileReader
from docopt import docopt
import Loger
import time
import re



import sys
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket



def load_config(category, key ):
    import ConfigParser
    import io
    with open(r'C:\Users\vladi\PycharmProjects\PriceTracker\config.ini') as f:
        sample_config = f.read()
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.readfp(io.BytesIO(sample_config))
    result= config.get(category, key)



    # parser = SafeConfigParser()
    # parser.read(r'C:\Users\vladi\PycharmProjects\PriceTracker\config.ini')
    # result = parser.get(category, key)#(parser.get('initialize', 'svc_path'),parser.get('initialize', 'time_out_in_min'))
    #
    # print result
    return result

def extract_itemID_from_ulr(url):
    return re.search(r'\d+', url).group()  # extract item id from url

def main_func(path):
    Loger.logger.info('Start check prices')
    # define the suppliers dictionary when the key is the supplier name
    suppliers = {'gearbest': GearBest.Gearbest(), 'dx': DX.DX(), 'tmart': TMart.Tmart()}
    ebay = Ebay(load_config('Ebay', 'appid'), load_config('Ebay', 'certid'), load_config('Ebay', 'devid'),
                load_config('Ebay', 'token'))

    #arguments = docopt(__doc__)
    # initialize the csv reader with path from command line argument
    file_reader = CSVFileReader(path)#(arguments['<path>'])



        # read the csv file
    lists = file_reader.read()
    for list in lists:  # iterate the all item
        # Check stock
        if list.ebay_url <> '':
            is_in_stock = suppliers[list.supplier.lower()].is_in_stock(list.url)
            item_id = extract_itemID_from_ulr(list.ebay_url)
            ebay.update_staock(item_id, 1 if is_in_stock else 0)

        #get actual price from supplier site
        actual_price = suppliers[list.supplier.lower()].do_scraping(
            list.url)  # get actual price of item from the site
        if actual_price == -1:
            #failed to extract data from url
            Loger.logger.warning('Failed to scrap information from {}'.format(list.url))
            if list.ebay_url <> '':
                item_id = extract_itemID_from_ulr(list.ebay_url)
                ebay.update_staock(item_id, 0)  # save the new prise on ebay
        elif actual_price <> float(list.price):
            #the price has been changed
            if list.ebay_url<>'':
                item_id = extract_itemID_from_ulr(list.ebay_url)
                try:
                    to_price = ebay.get_ebay_price(item_id) + (actual_price-float(list.price))#calculate the new price

                except:
                    Loger.logger.error('Failed to get current ebay price for listing {}. Skipping the price comparing'.format(list.ebay_url))
                    continue
                Loger.logger.warn(
                    'The url {} price has been changed from {} to {}, change ebay price to {}'.format(list.ebay_url,
                                                                                                      list.price,
                                                                                                      actual_price,
                                                                                                      to_price))  # to do something
                list.price = actual_price # update a new price to save it at the end of for
                ebay.update_price(item_id,to_price)#save the new prise on ebay


    file_reader.write(lists)
    Loger.logger.info('Finished check prices')





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

        path, time_out = load_config('initialize', 'svc_path'), load_config('initialize', 'time_out_in_min')
        Loger.logger.info('The price tracker was started with time_out {}'.format(time_out))
        while self.isAlive:

            main_func(path)
            time.sleep(float(time_out)*60)


if __name__ == '__main__':
    #main_func(load_config('initialize', 'svc_path'))

    win32serviceutil.HandleCommandLine(AppServerSvc)