from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Users/Flip/Development/chromedriver"

ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)

driver.get(
    "https://www.amazon.com/all-new-fire-tv-stick-4k-with-alexa-voice-remote/dp/B08XVYZ1Y5/ref=sr_1_1?keywords=fire+stick&qid=1663695856&sr=8-1"
)

price = driver.find_element(by="class name", value="a-offscreen+span")
print(price.text)

driver.close()  ## Closes active tab
# driver.quit()  ## Closes whole browser
