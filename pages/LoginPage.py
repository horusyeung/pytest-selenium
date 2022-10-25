# This page contains the fixed locators and elements for Betta login page

from conf.conf import SecData
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """Input-box Elements"""
    USERNAME_INPUT = (By.XPATH, "/html/body/form/input[1]")
    PASSWORD_INPUT = (By.XPATH, "/html/body/form/input[2]")

    """Button Elements"""
    SIGN_IN_BUTTON = (By.XPATH, "/html/body/form/input[3]")

    """Elements for assertions"""
    EXAMPLE_LABEL = (By.XPATH, "/html/body/div/h1")

    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(SecData.BASE_URL)

    """Page Actions: Get"""

    def get_current_page_url(self):
        return self.get_current_url()

    def get_current_page_title(self, text):
        return self.get_title(text)

    def get_example_label_text(self):
        return self.get_text(self.EXAMPLE_LABEL)

    """Page Actions: Verification"""

    def is_text_exists(self):
        return self.is_visible(self.EXAMPLE_LABEL)

    """Page Actions: Do"""

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME_INPUT, username)
        self.do_send_keys(self.PASSWORD_INPUT, password)
        self.do_click(self.SIGN_IN_BUTTON)

