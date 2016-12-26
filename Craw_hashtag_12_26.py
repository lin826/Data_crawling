# Get 200 hosts randomly
#       except 1-300 (299 not found)  15800-16205 (15865 not found)  9600-9800
#       12000-12300 17000 - 17296
import csv
import re
import time

from selenium import webdriver
#Optional Packages
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

input_file = 'mybirthday.csv'
output_file = 'user_data.csv'

driver_get = webdriver.Firefox()

with open(input_file, 'rU') as file:
    file_content = csv.reader(file)
    with open(output_file, 'w') as csvfile:
        fieldnames = ['username','id','url','alt']
        spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
        spamwriter.writeheader()
        for row in csv.reader(file, delimiter=','):
            print(row[0])
            driver_get.get('https://www.instagram.com/'+row[0])
            for i in range(0,3):
                try:
                    driver_get.find_element_by_class_name("_oidfu").click() # more button
                    break
                except NoSuchElementException:
                    print('NoSuchElementException in driver_get for button more')
                    time.sleep(1)
            number = driver_get.find_element_by_class_name("_bkw5z").text # number of posts
            number = int(number.replace(',',''))
            previous = 0
            while(previous<number):
                driver_get.execute_script("window.scrollTo(0, document.body.scrollHeight/);")
                driver_get.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                e = driver_get.find_elements_by_class_name("_icyx7") # each item
                for index in range(previous,len(e)):
                    # driver_detail.get()
                    spamwriter.writerow({fieldnames[0]:row[0],
                    fieldnames[1]:e[index].get_attribute("id"),
                    fieldnames[2]:e[index].get_attribute("src"),
                    fieldnames[3]:(e[index].get_attribute("alt")).encode("utf-8")})
                previous = len(e)
