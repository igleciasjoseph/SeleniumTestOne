from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os, json, getpass, time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get('https://learn.codingdojo.com/signin')


iUser = input('Please enter your email for login without the @google.com ')
iEmail = '@gmail.com'
iPass = getpass.getpass()

browser.implicitly_wait(20)


elem = browser.find_element_by_id('enter_email')
elem.send_keys(iUser + iEmail)

elem = browser.find_element_by_id("enter_password")
elem.send_keys(iPass)

elem.send_keys(Keys.ENTER)


elem = browser.find_element_by_link_text("Python").click()



elem = browser.find_element_by_link_text("Proceed").click()


elem = browser.find_element_by_tag_name("body").click()
time.sleep(2)


elem = browser.find_element_by_tag_name("body").click()





time.sleep(5)
browser.quit()
