from time import sleep
from argparse import ArgumentParser
from selenium_session import load_session
from selenium_login import GenericBot
import os.path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def login():
    options = webdriver.ChromeOptions()
    options.binary_location = '/usr/bin/chromium'
    chrome_driver_binary = '/usr/bin/chromedriver'
    d = webdriver.Chrome(chrome_driver_binary, options=options)
    d.get('https://web.whatsapp.com/')
    return d


def select_contact(driver, to):
    wait = WebDriverWait(driver=driver, timeout=90)
    name_argument = f'//span[contains(@title,\'{to}\')]'
    title = wait.until(EC.presence_of_element_located(
        (By.XPATH, name_argument)))
    title.click()


def paste_message(driver):
    sleep(1)
    box = driver.find_element_by_xpath('//*[@spellcheck="true"]')
    box.send_keys(Keys.CONTROL + "v")

    sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()


def send_message(driver, message):
    sleep(1)
    box = driver.find_element_by_xpath('//*[@spellcheck="true"]')
    box.send_keys(message + Keys.ENTER)


bot_name = "webhook"
# You should remove this file when you exit, I'm still trying to find a better way to do it =)

if os.path.isfile(f"{bot_name}.json"):
    driver = load_session(bot_name)
    sleep(1)
else:
    bot = GenericBot(bot_name, "https://web.whatsapp.com/")
    bot.login()
    driver = bot.driver
    sleep(9)


parser = ArgumentParser()

parser.add_argument("-c", "--contact", dest="contact_name",
                    action='store', type=str,
                    help="Select wich contact to send an message", default=True)

parser.add_argument("-m", "--message",
                    dest="message_text", default=True,
                    action='store',
                    help="Message text to be sent")


parser.add_argument("-p", "--paste",
                    dest="pasted_content", action="store_true",
                    help="Paste content from clipboard instead of writing")

args = parser.parse_args()

# Usage:
# python3 -i selenium_whatsapp_bot.py -c "Anotações" -m "Teste"
if __name__ == "__main__":
    if args.contact_name is not None and args.pasted_content:
        select_contact(driver, args.contact_name)
        paste_message(driver)

    elif args.contact_name is not None and args.message_text is not None:
        select_contact(driver, args.contact_name)
        send_message(driver, args.message_text)

