# -*- coding: utf-8 -*-

'''
Created in 11/2019
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
import os
from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ChormeDriver https://chromedriver.chromium.org/

class FalseAPI():

    """
    -> Fake API for sending messages on WhatsApp
    """
 
    def __init__(self):
    
        """
        -> Initial access function\
        \n:return: Access to the main page
        """
        
        # config webdriver
        user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        self.options = webdriver.FirefoxOptions()
        #self.options.headless = True
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

        way = Path('src') # path to geckodriver
        gecko = way / 'geckodriver' # way to geckodriver
        
        # get executable driver
        self.driver = webdriver.Firefox(executable_path=gecko, options=self.options)
        
        # url for driver acess
        self.driver.get('https://web.whatsapp.com/')

        # waiting for access
        while True:

            # try to access
            try:
                self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label').click() # search button
                break
            
            # wait for access
            except:
                pass

    def typephrase(self, text, field):

        """
        -> To type letter by letter\
        \n:return: The most organic words
        """

        for letter in text: 
            
            field.send_keys(letter) # type the letter in the field
            sleep(0.09) # input time of each letter
        

    def sendMsg(self, contact, msg, amount=1, temp=0):

        """
        -> Send the message to a specific contact or group\
        \n:param contact: Specific contact or group\
        \n:param msg: Message to send\
        \n:param amount: Number of messages\
        \n:param temp: Response time in seconds\
        \n:return: Sending the message\
        """

        # research field
        field = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]') 
        field.clear()
        self.typephrase(contact, field) # type the search

        self.driver.find_element_by_xpath(f'//span[@title="{contact}"]').click() # select the chosen contact

        while amount > 0:

            # field for entering text
            field = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
            field.clear()

            self.typephrase(msg, field) # type the entering text

            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]').click() # send button

            amount -= 1

        
# running the fake API
exec = FalseAPI()

contact = 'Test Group!'
message = 'Hello World!!'
amount = 10

exec.sendMsg(contact, message, amount) # to send simple text messages

