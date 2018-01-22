
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import cred

browser = webdriver.Firefox()
browser.get("https://www.quora.com")
elem =browser.find_elements_by_name("email")
print (elem)
 
elem[1].send_keys(cred.email)
elem=browser.find_elements_by_name("password")
elem[1].send_keys(cred.password)
elem[1].send_keys(Keys.RETURN)
 
time.sleep(10)
                                                                   #First 15 Elements
xpath="//textarea[contains(@placeholder,'Search Quora')]"
elem=browser.find_element_by_xpath(xpath)
elem.send_keys(cred.string)

time.sleep(8)

xpath="//img[contains(@style,'radius:13px')]"
elem=browser.find_elements_by_xpath(xpath)
elem[0].click()
print ("got image element ")

time.sleep(10)

xpath="//a[contains(@action_click,'AnswerRemoveUpvote')]"   
elem=browser.find_elements_by_xpath(xpath)

for i in range(0,7,2):
	elem[i].click()
	print("clicked ") 

print ("got desired upvote element ")

time.sleep(10)

for i in range(8,15,2):
	elem[i].click()
	print("clicked ") 

print ("got desired upvote element ")

time.sleep(10)

for i in range(16,23,2):
	elem[i].click()
	print("clicked ") 

print ("got desired upvote element ")
time.sleep(10)

for i in range(24,29,2):
	elem[i].click()
	print("clicked ") 

print ("got desired upvote element ")
time.sleep(10)
browser.execute_script("window.scrollTo(0, 1980)")
time.sleep(10)
																#Next 15 Elements
xpath="//a[contains(@action_click,'AnswerRemoveUpvote')]"   
elem=browser.find_elements_by_xpath(xpath)
time.sleep(5)
for i in range(30,37,2):
	elem[i].click()
	print("clicked ") 

print ("got desired upvote element ")
time.sleep(10)

for i in range(38,45,2):
	elem[i].click()
	print("clicked ") 

print ("got desired upvote element ")
time.sleep(10)

for i in range(46,53,2):
	elem[i].click()
	print("clicked ") 

print ("got desired upvote element ")
time.sleep(10)

for i in range(54,59,2):
	elem[i].click()
	print("clicked ") 



time.sleep(10)
browser.execute_script("window.scrollTo(0, 1980)")
time.sleep(10)
																#Next 15 Elements
xpath="//a[contains(@action_click,'AnswerRemoveUpvote')]"   
elem=browser.find_elements_by_xpath(xpath)
time.sleep(5)

for i in range(60,67,2):
	elem[i].click()
	print("clicked ") 

print ("got desired upvote element ")
time.sleep(10)

for i in range(68,75,2):
	elem[i].click()
	print("clicked ") 

print ("got desired upvote element ")
time.sleep(10)

for i in range(76,83,2):
	elem[i].click()
	print("clicked ") 

print ("got desired upvote element ")
time.sleep(10)

for i in range(84,89,2):
	elem[i].click()
	print("clicked ") 

driver.close()