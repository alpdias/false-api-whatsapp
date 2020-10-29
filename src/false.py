# -*- coding: utf-8 -*-

'''
Created in 11/2019
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
import os
from time import sleep
from selenium import webdriver

# ChormeDriver https://chromedriver.chromium.org/

class FalseAPI():
 
    def __init__(self):
    
        """
        ->
        :return:
        """
        
        # config webdriver
        user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user_agent={user_agent}')
        #self.options.add_argument('--window-size=1366,768')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--alow-running-insecure-content')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('--proxy-server="direct://"')
        self.options.add_argument('--proxy-bypass-list=*')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        
        # get executable driver
        self.driver = webdriver.Chrome(executable_path='chromedriver', options=self.options)
        
        # url for driver acess
        self.driver.get('https://web.whatsapp.com/')
        print(self.driver.title)
        
        
    def head():
        
        """
        -> Browser with head to view actions
        :return: Actions taken by the driver
        """
        
        # get driver
        driver = webdriver.Firefox()
        
        # url for driver acess
        driver.get('https://web.whatsapp.com/') 
        


whatsapp = FalseAPI()

whatsapp.head()
