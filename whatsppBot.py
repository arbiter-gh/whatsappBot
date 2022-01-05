from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(20)
def start_messaging(path = '//span[@title = "wBot"]'):
    wbot = driver.find_element_by_xpath(path)
    wbot.click()   
    msg = driver.find_element_by_xpath('//div[@class = "_13NKt copyable-text selectable-text"][@data-tab = "9"]')
    with open('wallE.txt','r') as f:
        for word in f :
            msg.send_keys(word)

start_messaging()
