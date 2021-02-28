from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://localhost"

    def open_page(self, additional_url=''):
        self.driver.get(self.base_url + additional_url)
        return self.driver

    def get_element(self, selector, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(selector))

    def get_elements(self, selector, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(selector))

    def mouse_click_to_element(self, element):
        ActionChains(self.driver).move_to_element(element).click().perform()

    def get_element_text(self, element):
        return element.text.strip()

    def set_text(self, element, value):
        element.clear()
        element.send_keys(value)
