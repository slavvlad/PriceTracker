from unicodedata import decimal

from ebaysdk.finding import Connection as finding
from ebaysdk.trading import Connection as Trading

class Ebay:
    def __init__(self,appid,certid,devid, token):
        self.appid = appid
        self.certid = certid
        self.devid = devid
        self.token = token
        self.site = 'EBAY-US'

    def update_price(self,item_id,to_price):
        tranding_api = Trading(config_file=None, appid=self.appid, certid=self.certid, token=self.token)
        request = {'Item':{'ItemID':item_id,'StartPrice':to_price}}
        tranding_api.execute('ReviseFixedPriceItem', request)



    def get_ebay_price(self,item_id):
        tranding_api = Trading(config_file=None, appid=self.appid, certid=self.certid, token=self.token)
        storeData = {
            #'MessageID': 'IT CIRCLE CONSULT PYTHON - MAFFAS',
            'ItemID': item_id,
        }
        response = tranding_api.execute('GetItem', storeData)
        item_deatails = response.dict()['Item']
        return float(item_deatails['StartPrice']['value'])