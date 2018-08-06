import Scraping
from Singleton import Singleton
import re

# @Singleton
class Gearbest(Scraping.Scraping):

    def do_scraping(self, url):
        result = super(Gearbest,self).do_scraping(url)
        text= result.text.lstrip().splitlines()[0]
        return float(re.findall(r"\d+\.\d+", text)[0])

        # tables = soup.find_all('table')
        # for table in tables:
        #     df = pd.read_html(str(table))
        #     # print(df[0].to_json(orient='records')+"\n\n")
        #     print (tabulate(df[0], headers='keys', tablefmt='psql'))
