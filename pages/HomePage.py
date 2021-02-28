from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class HomePage(BasePage):
    """Главная страница"""

    @property
    def opencart_logo(self):
        return self.get_element((By.CSS_SELECTOR, '#logo'))

    @property
    def featured_products(self):
        return self.get_elements((By.CSS_SELECTOR, '.product-layout .caption a'))

    def get_featured_product_name_by_index(self, index):
        return self.get_element_text(self.featured_products[index])

    def click_featured_product(self, index):
        self.mouse_click_to_element(self.featured_products[index])

    def add_to_cart_featured_product(self, index):
        add_to_cart = self.get_elements((By.CSS_SELECTOR, 'button[onclick*=cart]'))
        self.mouse_click_to_element(add_to_cart[index])
