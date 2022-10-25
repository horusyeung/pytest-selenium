# This page contains all the generic methods and utilities of all the pages

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 3)

    """get actions"""

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self, text):
        self.wait.until(EC.title_is(text))
        return self.driver.title

    def get_attribute(self, locator, attribute):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.actions.move_to_element(element).perform()
        return element.get_attribute(attribute)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.actions.move_to_element(element).perform()
        return element.text

    """is actions"""

    def is_visible(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.actions.move_to_element(element).perform()
        return bool(element)

    def is_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element(locator))

    """do actions"""

    def do_click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.actions.move_to_element(element).click().perform()

    def do_send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    def do_clear_input(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()

    def do_move_to(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.actions.move_to_element(element).perform()
