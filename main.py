import multiprocessing
import shutil
import sys
from calendar import c
from itertools import count
from operator import le
from xml.dom.minidom import Document
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import random
import socket

from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementClickInterceptedException,
    WebDriverException,
    TimeoutException,
)
import pyautogui
import pyperclip
import csv
import pandas as pd
from glob import glob
import os
import random
from selenium.webdriver.common.keys import Keys
import requests
import pathlib
from selenium.webdriver.common.action_chains import ActionChains
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def is_connected():
    hostname = "one.one.one.one"
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(hostname)
        # connect to the host -- tells us if the host is actually reachable
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except Exception:
        pass  # we ignore any errors, returning False
    return False


def xpath_soup(element):
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name
            if siblings == [child] else
            '%s[%d]' % (child.name, 1 + siblings.index(child))
        )
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)


def write_category(category, driver, wordpress_link, current_title):
    driver.find_element(By.TAG_NAME, "textarea").click()
    driver.find_element(By.TAG_NAME, "textarea").send_keys(
        f'Give me in list. The blog you have  just  written falls  in which categories within the following categories : {category}.')
    time.sleep(2)
    driver.find_element(By.TAG_NAME, "textarea").send_keys(Keys.RETURN)
    time.sleep(5)


def main():
    # profile_file_name = input("Output file  name  without (.csv) = ")
    # Open the file in read mode ('r')
    with open('message.txt', 'r', encoding='utf-8') as file:
        # Read the contents of the file
        content = file.read()


    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)  # version_main allows to specify your chrome version instead of following chrome global version
    driver.maximize_window()
    driver.get("https://twitter.com/i/flow/login")
    print("Put your cursor  from where  you want to scrap.")
    my_input = input("Enter the 'S' after  login and you are  in homepage : ")

    if my_input == 'S':
      # Load the CSV file into a pandas DataFrame
      df = pd.read_csv('Test.csv')
      base_url = 'https://twitter.com'

      # Iterate over each row in the DataFrame
      for index, row in df.iterrows():
        # Get the profile link
        profile_link = row['tweeter_profile_link']
            
        # Construct the full URL
        full_url = base_url + profile_link
            # Navigate to the profile
        driver.get(full_url)

        try:
            while True:
                find_userName = None
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')

                find_userName = soup.find(attrs={"data-testid": "UserName"})   

                if find_userName != None:
                    break
            
            time.sleep(2)
            
            message_btn = None
            message_btn = soup.find(attrs={"data-testid": "sendDMFromProfile"})    
            
            driver.find_element(By.XPATH,xpath_soup(message_btn)).click()
            
            while True:
                find_messageBox = None
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')

                find_messageBox = soup.find(attrs={"data-testid": "dmComposerTextInput"})   

                if find_messageBox != None:
                    break
            
            print(find_messageBox)
            driver.find_element(By.XPATH,xpath_soup(find_messageBox)).click()
            time.sleep(2)
            print(find_messageBox)

            driver.find_element(By.XPATH,xpath_soup(find_messageBox)).send_keys(content)
                
                
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            send_message_btn = soup.find(attrs={"data-testid": "dmComposerSendButton"})
            

            driver.find_element(By.XPATH, xpath_soup(send_message_btn)).click()
            
            time.sleep(2)
            
            

        except Exception as e:
            print(f"Exception occurred: {e}")


if __name__ == '__main__':
    try:
        main()
    except:
        print("Done")
        raise
