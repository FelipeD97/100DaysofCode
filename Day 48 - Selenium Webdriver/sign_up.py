from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = "/Users/Flip/Development/chromedriver"

ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(by="name", value="fName")
lname = driver.find_element(by="name", value="lName")
email = driver.find_element(by="name", value="email")
submit = driver.find_element(by="tag name", value="button")

fname.send_keys("Flip")
time.sleep(2)
lname.send_keys("Dun")
time.sleep(2)
email.send_keys("flipdun@email.com")
time.sleep(2)
submit.click()

