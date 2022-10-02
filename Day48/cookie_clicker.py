from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = "/Users/Flip/Development/chromedriver"

ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

### Cookie element ###
cookie = driver.find_element(by="css selector", value="#cookie")

### Get upgrade item ids ###
items = driver.find_elements(by="css selector", value="#store div")
item_ids = [item.get_attribute("id") for item in items]

### Timers ###
timeout = time.time() + 5
five_min = time.time() + (60 * 5)

while True:
    cookie.click()

    if time.time() > timeout:

        store = driver.find_elements(by="css selector", value="#store b")
        item_prices = []

        for price in store:
            element_text = price.text
            if element_text != "":
                cost = element_text.split("-")[1].strip().replace(",", "")
                item_prices.append(cost)

        # print(item_prices)

        upgrade_list = {}
        for n in range(len(item_prices)):
            upgrade_list[item_prices[n]] = item_ids[n]

        # print(upgrade_list)

        money_element = driver.find_element(by="css selector", value="#money")
        cookie_count = int(money_element.text.replace(",", ""))

        affordable_upgrades = {}
        for cost, id in upgrade_list.items():
            if cookie_count > int(cost):
                affordable_upgrades[cost] = id

        highest_purchase = max(affordable_upgrades)
        print(highest_purchase)
        to_purchase_id = affordable_upgrades[highest_purchase]

        driver.find_element(by="id", value=to_purchase_id).click()
        timeout = time.time() + 5

