from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ProductPage(BasePage):
    """Карточка продукта"""

    additional_url = '/index.php?route=product/product&path=57&product_id=49'

    def open(self):
        return self.open_page(additional_url=self.additional_url)

    def get_product_name(self):
        element = self.get_element((By.CSS_SELECTOR, '#content h1'))
        return self.get_element_text(element)

    def get_product_price(self):
        element = self.get_element((By.XPATH, "//*[@id='content']//ul//h2"))
        return self.get_element_text(element)

    def set_quantity(self, value):
        element = self.get_element((By.CSS_SELECTOR, 'input[name="quantity"]'))
        return self.set_text(element, value)

    def add_to_cart(self):
        add_to_cart_button = self.get_element((By.CSS_SELECTOR, '#button-cart'))
        return self.mouse_click_to_element(add_to_cart_button)
