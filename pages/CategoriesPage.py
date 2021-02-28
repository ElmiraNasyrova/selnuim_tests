from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CategoriesPage(BasePage):
    """Каталог товаров"""

    additional_url = '/index.php?route=product/category&path=20'

    def open(self):
        return self.open_page(additional_url=self.additional_url)

    def get_category_name(self):
        element = self.get_element((By.CSS_SELECTOR, '#content h2'))
        return self.get_element_text(element)

    @property
    def product_minicard(self):
        return self.get_element((By.CSS_SELECTOR, '.product-thumb .caption h4 a'))

    def get_product_name_in_minicard(self):
        return self.get_element_text(self.product_minicard)

    def open_product_card(self):
        return self.mouse_click_to_element(self.product_minicard)
