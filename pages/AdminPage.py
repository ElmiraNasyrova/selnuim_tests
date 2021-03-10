from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AdminPage(BasePage):
    """Старница авторизации"""

    additional_url = '/admin/'

    def open(self):
        return self.open_page(additional_url=self.additional_url)

    @property
    def username(self):
        return self.get_element((By.CSS_SELECTOR, "[name='username']"))

    @property
    def password(self):
        return self.get_element((By.CSS_SELECTOR, "[name='password']"))

    @property
    def login_button(self):
        return self.get_element((By.CSS_SELECTOR, "[type='submit']"))

    def login(self, username, password):
        self.set_text(self.username, username)
        self.set_text(self.password, password)
        self.mouse_click_to_element(self.login_button)

    def logout(self):
        element = self.get_element((By.XPATH, "//*[contains(@class, 'sign-out')]"))
        self.mouse_click_to_element(element)

    def open_products(self):
        catalog_button = self.get_element((By.CSS_SELECTOR, "#menu-catalog"))
        self.mouse_click_to_element(catalog_button)

        products_button = self.get_element((By.XPATH, "//*[@id='menu-catalog']//*[contains(text(), 'Products')]"))
        self.mouse_click_to_element(products_button)

    @property
    def table(self):
        return self.get_element((By.CSS_SELECTOR, "table"))
