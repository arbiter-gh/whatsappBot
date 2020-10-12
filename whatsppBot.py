from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wBot(path = '//span[@title = "wBot"]'):
    driver = webdriver.Firefox()
    driver.get("https://web.whatsapp.com/")
    try:
        wbot = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,path)))
        wbot = driver.find_element_by_xpath(path)
        wbot.click()
        msg = driver.find_element_by_xpath('//div[@class = "_3FRCZ copyable-text selectable-text"][@data-tab = "1"]')

    finally: 
       pass

wBot()