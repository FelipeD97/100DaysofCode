from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/Flip/Development/chromedriver"

ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles = driver.find_element(by="xpath", value='//*[@id="articlecount"]/a[1]')
articles = driver.find_element(by="css selector", value="#articlecount a")
# print(articles.text)
# articles.click()

community_portal = driver.find_element(by="link text", value="Community portal")
# community_portal.click()

search = driver.find_element(by="name", value="search")
search.send_keys("Young avengers")
search.send_keys(Keys.ENTER)

# suggestions = driver.find_element(by="css selectors", value=".suggestions-results a")
# suggestions.click()
# driver.close()
