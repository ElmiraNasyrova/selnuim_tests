import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demo.opencart.com/"
        self.logger = logging.getLogger(type(self).__name__)

    def open_page(self, additional_url=''):
        self.logger.info(f"Opening url: {self.base_url + additional_url}")
        self.driver.get(self.base_url + additional_url)
        return self.driver

    def get_element(self, selector, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(selector))

    def get_elements(self, selector, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(selector))

    def mouse_click_to_element(self, element):
        self.logger.info(f"Clicking element: {element}")
        ActionChains(self.driver).move_to_element(element).click().perform()

    def get_element_text(self, element):
        self.logger.info(f"Get text of {element}")
        return element.text.strip()

    def set_text(self, element, value):
        self.logger.info(f"Input {value} in input {element}")
        element.clear()
        element.send_keys(value)
