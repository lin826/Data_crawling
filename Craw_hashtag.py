# Get encode way
import urllib
import chardet
import csv
import json
import re
import time
import sys

from selenium import webdriver
#Optional Packages
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

reload(sys)
sys.setdefaultencoding('utf-8')

input_file = 'id.csv'
output_file = 'user_data.json'

user_id = 'datascienceisgood'
user_pwd = 'datascience'

driver_get = webdriver.Firefox()

# Login
driver_get.get('https://www.instagram.com/accounts/login/')
time.sleep(2)
driver_get.find_element_by_xpath('//input[@name="username"]').send_keys(user_id)
driver_get.find_element_by_xpath('//input[@name="password"]').send_keys(user_pwd)
driver_get.find_element_by_class_name('_aj7mu').click()
time.sleep(5)


with open(input_file, 'rU') as file:
    file_content = csv.reader(file)
    with open(output_file, 'w') as outfile:
        data = list()
        for row in csv.reader(file, delimiter=','):
            if(row[0]=='username'):
                continue
            url_user_page = 'https://www.instagram.com/'+row[0]
            driver_get.get(url_user_page)
            number = 0
            item = {'user_id':row[0],'pictures':list()}
            for i in range(0,3): # prevent for webpage loading
                try:
                    driver_get.find_element_by_class_name("_oidfu").click() # more button
                    number = driver_get.find_element_by_class_name("_bkw5z").text # number of posts
                    number = int(number.replace(',',''))
                    break
                except NoSuchElementException:
                    print('NoSuchElementException in driver_get for button more')
                    time.sleep(1)
            previous = 0
            while(previous<number):
                driver_get.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
                time.sleep(1)
                driver_get.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                e = driver_get.find_elements_by_class_name("_icyx7") # each item
                href = driver_get.find_elements_by_class_name("_8mlbc") # each item
                for index in range(previous,len(e)):
                    node = {}
                    node['post_url'] = href[index].get_attribute('href')
                    node['picture_url'] = e[index].get_attribute("src")
                    tags = e[index].get_attribute("alt")
                    node['hashtags'] = [tag.strip("#") for tag in tags.split() if tag.startswith("#")]
                    item['pictures'].append(node)
                    # http://stackoverflow.com/questions/6331497/an-elegant-way-to-get-hashtags-out-of-a-string-in-python
                previous = len(e)
                if(previous==0):
                    break
            data.append(item)
        json.dump(data, outfile)
