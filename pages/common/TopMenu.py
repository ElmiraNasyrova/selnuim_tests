from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class TopMenu(BasePage):
    """Верхнее меню"""

    @property
    def cart(self):
        return self.get_element((By.CSS_SELECTOR, '#cart-total'))

    def click_to_cart(self):
        self.mouse_click_to_element(self.cart)

    def get_cart_text(self):
        return self.get_element_text(self.cart)

    def get_added_product_name(self):
        added_product = self.get_element((By.CSS_SELECTOR, '.dropdown-menu table'))
        return self.get_element_text(added_product)

    def logout(self):
        my_account = self.get_element((By.CSS_SELECTOR, '#top-links .dropdown'))
        self.mouse_click_to_element(my_account)
        account_menu = self.get_elements((By.CSS_SELECTOR, '#top-links .dropdown-menu li'))
        self.mouse_click_to_element(account_menu[4])
