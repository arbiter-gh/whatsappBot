from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wBot(path):
    driver = webdriver.Firefox()
    driver.get("https://web.whatsapp.com/")
    try:
        wbot = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,path)))
        wbot = driver.find_element_by_xpath(path)
        wbot.click()
        msg = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
        f = open('wallE.txt', 'r')
        for word in f:
            msg.send_keys(word)
            msg.send_keys(Keys.RETURN)
    finally:
        driver.close()