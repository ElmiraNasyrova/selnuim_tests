from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class Alert(BasePage):
    """алерты"""

    @property
    def alert(self):
        return self.get_element((By.CSS_SELECTOR, '.alert'))
