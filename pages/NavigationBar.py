from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class NavigationBar(BasePage):
    """Панель навигации"""

    def open_section_by_name(self, section_name):
        section = self.get_element((By.LINK_TEXT, section_name))
        return self.mouse_click_to_element(section)
