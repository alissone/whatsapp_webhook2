
import json
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def attach_to_session(executor_url, session_id):
    original_execute = WebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)
    # Patch the function before creating the driver object
    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities={})
    driver.session_id = session_id
    # Replace the patched function with original function
    WebDriver.execute = original_execute
    return driver


def save_session(driver, filename="session"):
    """
    Saves current session info into a json file to allow Selenium to connect to
    an existing window remotely
    """
    session = {}
    session["url"] = driver.command_executor._url # TODO: Find another way to get _url
    session["id"] = driver.session_id

    with open(filename + ".json", "w") as session_file:
        json.dump(session, session_file, sort_keys=True, indent=4)


def load_session(filename="session"):
    """
    Loads a webdriver session from a json file created using `save_session`
    """
    with open(filename + ".json", "r") as session_file:
        session = json.load(session_file)

    print(session["url"])
    driver = attach_to_session(session["url"], session["id"])
    return driver


def build_driver(new_session=True):
    """
    Creates a selenium chrome webdriver session if it does not exist yet
    """
    options = webdriver.ChromeOptions()
    options.binary_location = '/usr/bin/chromium'
    chrome_driver_binary = '/usr/bin/chromedriver'
    options.add_experimental_option("detach", True)

    if new_session:
        return webdriver.Chrome(chrome_driver_binary, options=options)
    return webdriver.Remote(chrome_driver_binary, options=options)
