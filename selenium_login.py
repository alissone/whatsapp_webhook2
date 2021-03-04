import time
import random
from selenium_session import build_driver, load_session, save_session


class GenericBot():
    """
    A generic class to allow interactive use of selenium with a single session
    """

    def __init__(self, name, home_url):
        self.driver = build_driver(new_session=True)
        self.name = name
        self.home_url = home_url

    def verify_if_logged_in(self) -> bool:
        """Verify if user is already logged in. Should be overriden.

        Args:
            driver (webdriver): selenium webriver
        Returns:
            bool: True if the user has already logged in
        """
        try:
            return True

        except Exception as e:
            return False

    def login_function(self) -> bool:
        """Attempts to login on the page. Also store username and password
        somewhere. Should be overriden.

        Returns:
            bool: True if the login was successfull
        """
        print("Logging in...")

        try:
            print("Logged in sucessfully...")

            return True

        except Exception as e:
            print("Could not login because of", e)

            return False

    def open_url(self, url, wait=1):
        """
        Open a url waiting some delay
        """
        print("Navigating to", url, "...")
        self.driver.get(url)
        time.sleep(wait + (random.randint(0, 9) / 10))

    def login(self):
        """
        Login and save a session to be used later
        """
        self.open_url(self.home_url)

        logged_in = self.verify_if_logged_in()

        if not logged_in:
            self.login_function()

        save_session(self.driver, self.name)
