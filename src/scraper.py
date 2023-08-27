import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import helper

from pprint import pprint


ROOT_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class UnclaimedFundReconciliationScraperException(Exception):
    def __init__(self, message="A custom error occurred"):
        self.message = message
        super().__init__(self.message)

class Scraper():
    
    def __init__(self,
                webdriver_path : str = "/usr/local/bin/chromedriver",
                ) -> None:
      
        self.webdriver_path = webdriver_path
        self.webdriver_ = None
        self.TexasUnclaimedPropertyURL = "https://www.claimittexas.gov/"
        self.htmlOutputPath_basesite = 'output/TexasUnclaimedPropertySite.html'
        self.renew_chrome_webdriver()
        

    def renew_chrome_webdriver(self, webdriver_path = None):
        cur_webdriver_path = self.webdriver_path if not webdriver_path else webdriver_path

       # create webdriver
        try:
            self.webdriver_ = webdriver.Chrome(
                keep_alive=True,
            )
            
        except UnclaimedFundReconciliationScraperException as err:
            raise(err)
    
    def getUnclaimedFundsSite_local(self, save_output: bool = False):
        if not self.webdriver_:
            self.renew_chrome_webdriver()  # Initialize the webdriver if it's None
        
        try:
            self.webdriver_.get(self.TexasUnclaimedPropertyURL)
        except UnclaimedFundReconciliationScraperException as err:
            raise(err)
        
        
        helper.save_html(
            self.webdriver_.page_source.encode('utf-8'),
            os.path.join(ROOT_FOLDER,self.htmlOutputPath_basesite)) if save_output else None
        
    
    def querySearchForm():
        pass

        
if __name__ == "__main__":
    myscraper = Scraper()
    myscraper.getUnclaimedFundsSite_local()
    print('done')