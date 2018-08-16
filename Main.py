'''Usage:
  main.py path <path> timer <timer>


Options:
  -h --help     Show this screen.
  <timer> timer to sleep in minuets

'''
from EbaySource import Ebay
from Suppliers import GearBest, DX
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
    from ConfigParser import SafeConfigParser
    parser = SafeConfigParser()
    parser.read(r'C:\Users\vladi\PycharmProjects\PriceTracker\config.ini')
    result = parser.get(category, key)#(parser.get('initialize', 'svc_path'),parser.get('initialize', 'time_out_in_min'))
    print result
    return result

def main_func(path):
    Loger.logger.info('The price tracker was started')
    # define the suppliers dictionary when the key is the supplier name
    suppliers = {'gearbest': GearBest.Gearbest(), 'dx': DX.DX()}
    ebay = Ebay(load_config('Ebay','appid'), load_config('Ebay','certid'), load_config('Ebay','devid'), load_config('Ebay','token'))

    #arguments = docopt(__doc__)
    # initialize the csv reader with path from command line argument
    file_reader = CSVFileReader(path)#(arguments['<path>'])



        # read the csv file
    lists = file_reader.read()
    for list in lists:  # iterate the all item

        actual_price = suppliers[list.supplier.lower()].do_scraping(
            list.url)  # get actual price of item from the site
        if actual_price <> float(list.price):
            #the price has been changed
            if list.ebay_url<>'':
                item_id = re.search(r'\d+', list.ebay_url).group() #extruct item id from url
                try:
                    to_price = ebay.get_ebay_price(item_id)+ (actual_price-float(list.price))#calculate the new price

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
        path, time_out = load_config('initialize', 'svc_path'), load_config('initialize', 'time_out_in_min')
        while self.isAlive:

            main_func(path)
            time.sleep(float(time_out)*60)

if __name__ == '__main__':
    #main_func(load_config('initialize', 'svc_path'))

     win32serviceutil.HandleCommandLine(AppServerSvc)