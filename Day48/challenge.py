from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Users/Flip/Development/chromedriver"

ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)

driver.get("https://www.python.org/")

event_times = driver.find_elements(by="css selector", value=".event-widget time")
event_names = driver.find_elements(by="css selector", value=".event-widget li a")

events = {}

for index in range(len(event_times)):
    events[index] = {"time": event_times[index].text, "name": event_names[index].text}

print(events)

driver.close()
