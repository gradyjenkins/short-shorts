import requests
import pprint
from bs4 import BeautifulSoup
from requests_html import HTMLSession

from models.table_data import TableData
from models.company_data import CompanyData

class DataDownloader():
    def __init__(self):
        self._url_highlites_nyse = r'http://www.wsj.com/mdc/public/page/2_3062-nyseshort-highlites.html'
        self._url_highlites_nyseAmerican = r'http://www.wsj.com/mdc/public/page/2_3062-amexshort-highlites.html'
        self._url_highlites_nasdaq = r'http://www.wsj.com/mdc/public/page/2_3062-nasdaqshort-highlites.html'
        self._url_company = r'http://www.wsj.com/mdc/public/page/2_3062-shtnyse_0_9-listing.html'
        self.session = HTMLSession()

    def get_highlite_data(self, exchange):
        """Gets the data for highlite sheet for NYSE.
        
        """
        url = self.get_url(exchange)
        page = self.session.get(url)
        res = {}
        for title in page.html.find('.mdcSubtbl'):
            st = []
            for table in page.html.find('.mdcTable'):
                for tr in table.find('tr'):
                    st.append(tr.text.split('\n'))
            res[title.text] = st
            
    def get_url(self, exchange):
        if exchange == 'nyse':
            return self._url_highlites_nyse
        if exchange == 'nasdaq':
            return self._url_highlites_nasdaq
        else:
            return self._url_highlites_nyseAmerican

if __name__ == '__main__':
    d = DataDownloader()
    d.get_highlite_data("nyse")