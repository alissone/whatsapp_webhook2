from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login():
    options = webdriver.ChromeOptions()
    options.binary_location = '/usr/bin/chromium'
    chrome_driver_binary = '/usr/bin/chromedriver'
    d = webdriver.Chrome(chrome_driver_binary, options=options)
    d.get('https://web.whatsapp.com/')
    return d

def select_contact(driver, to):
    wait = WebDriverWait(driver = driver, timeout = 90)	
    name_argument = f'//span[contains(@title,\'{to}\')]'
    title = wait.until(EC.presence_of_element_located((By.XPATH,name_argument)))
    title.click()

from time import sleep
def send_message(driver, message):
    sleep(1)
    box = driver.find_element_by_xpath('//*[@spellcheck="true"]')
    sleep(1)
    box.send_keys(message + Keys.ENTER)


# driver = login()
import os.path
from selenium_login import GenericBot
from selenium_session import load_session
bot_name = "webhook" 


if os.path.isfile(f"{bot_name}.json"):
    driver = load_session(bot_name)
else:
    bot = GenericBot(bot_name, "https://web.whatsapp.com/")
    bot.login()
    driver = bot.driver




sleep(9)
select_contact(driver, "Anotações")
send_message(driver, "Nova Instância")
