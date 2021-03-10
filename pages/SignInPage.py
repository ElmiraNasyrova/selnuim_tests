from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class SignInPage(BasePage):
    """Старница авторизации"""

    additional_url = '/index.php?route=account/login'

    def open(self):
        return self.open_page(additional_url=self.additional_url)

    def confirm_logout(self):
        element =  self.get_element((By.CSS_SELECTOR, ".buttons div a"))
        return self.mouse_click_to_element(element)

    @property
    def email_input(self):
        return self.get_element((By.CSS_SELECTOR, "#input-email"))

    @property
    def password_input(self):
        return self.get_element((By.CSS_SELECTOR, "#input-password"))

    @property
    def login_button(self):
        return self.get_element((By.CSS_SELECTOR, "input[type='submit']"))

    def login(self, email, password):
        self.set_text(self.email_input, email)
        self.set_text(self.password_input, password)
        self.mouse_click_to_element(self.login_button)

    def get_available_actions_header(self):
        header = self.get_element((By.CSS_SELECTOR, "#content h2"))
        return self.get_element_text(header)
