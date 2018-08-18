import Scraping
from Singleton import Singleton
import re

# @Singleton
class Gearbest(Scraping.Scraping):

    @Scraping.catch_exceptions
    def do_scraping(self, url):
        result = super(Gearbest,self).do_scraping(url)
        name_box = result.find(attrs={"class": "price-loading goodsIntro_price js-currency js-panelIntroPrice"})
        #text= result.text.lstrip().splitlines()[0]
        return float(re.findall(r"\d+\.\d+", name_box.text)[0])

        # tables = soup.find_all('table')
        # for table in tables:
        #     df = pd.read_html(str(table))
        #     # print(df[0].to_json(orient='records')+"\n\n")
        #     print (tabulate(df[0], headers='keys', tablefmt='psql'))
