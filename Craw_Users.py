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

hashtag_to_search = "mybirthday"
output_file = hashtag_to_search+'.csv'

baseurl = "https://www.instagram.com/accounts/login/"
username="Scientistest"
password="DataScience"



# search tag
driver_rand = webdriver.Firefox()
driver_rand.get('https://www.instagram.com/explore/tags/'+hashtag_to_search)
# get information
driver_get = webdriver.Firefox()

# Click on "More"
i=0
number=0
while(i<10):
	try:
		number = driver_rand.find_element_by_class_name("_bkw5z").text
		number = int(number.replace(',',''))
		driver_rand.find_element_by_class_name("_oidfu").click()
		break
	except NoSuchElementException:
		i+=1
		time.sleep(3)
		print('NoSuchElementException')
print(number)



# Get photos information and insert into the csv file
# First time to runnin

with open(output_file, 'w') as csvfile:
	fieldnames = ['username','datetime','location','photo_url']
	spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
	spamwriter.writeheader()
	# Scroll down to get all results
	previous=0
	for i in range(0,10): # retry when there's NoSuchElementException
		try:
			e = driver_rand.find_elements_by_class_name("_8mlbc")
			for index in range(previous,len(e)):
				url = e[index].get_attribute("href")
				driver_get.get(url)
				for j in range(0,10): # retry when there's NoSuchElementException
					try:
						name = driver_get.find_element_by_class_name("_4zhc5").get_attribute("title")
						date = driver_get.find_element_by_class_name("_379kp").get_attribute("datetime")
						try:
							location = driver_get.find_element_by_class_name("_kul9p").get_attribute("href")
						except NoSuchElementException:
							location = ""
						print(index)
						print('	'+name+'	'+date+'	'+location+'	'+url)
						spamwriter.writerow({fieldnames[0]:name,
							fieldnames[1]:date,fieldnames[2]:location,
							fieldnames[3]:url})
						break
					except NoSuchElementException:
						print('NoSuchElementException in driver_get')
						driver_rand.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			if(len(e)>number):
				break
			else:
				previous=len(e)
				print(len(e))
			driver_rand.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		except NoSuchElementException:
			driver_rand.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			print('NoSuchElementException in driver_rand')


# Have previous data
'''
with open(output_file, 'rU') as file:
	file_content = csv.reader(file)
	with open(output_file, 'w') as csvfile:
		fieldnames = file_content.next()
		spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
		spamwriter.writeheader()
		# Put previous data back
		for row in file_content:
			spamwriter.writerow({fieldnames[0]:row[0],
				fieldnames[1]:row[1],
				fieldnames[2]:row[2],
				fieldnames[3]:row[3]})
'''
