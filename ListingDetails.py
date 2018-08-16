
class ListingDetails:
    header = ['supplier', 'url', 'price', 'shipping']
    def __init__(self,supplier,url,ebay_url, price,shipping,is_in_stock):
        self.supplier = supplier
        self.url = url
        self.ebay_url = ebay_url
        self.price = price
        self.shipping = shipping
        self.is_in_stock = is_in_stock

    def __iter__(self):
        yield 'supplier', self.supplier
        yield 'url', self.url
        yield 'ebay_url', self.ebay_url
        yield 'price', self.price
        yield 'shipping', self.shipping
        yield 'is_in_stock', self.is_in_stock
