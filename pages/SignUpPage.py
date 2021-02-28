from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class SignUpPage(BasePage):
    """Старница регистрации"""

    additional_url = '/index.php?route=account/register'

    def open(self):
        return self.open_page(additional_url=self.additional_url)

    @property
    def first_name(self):
        return self.get_element((By.CSS_SELECTOR, "input[name='firstname']"))

    @property
    def last_name(self):
        return self.get_element((By.CSS_SELECTOR, "input[name='lastname']"))

    @property
    def email(self):
        return self.get_element((By.CSS_SELECTOR, "input[name='email']"))

    @property
    def telephone(self):
        return self.get_element((By.CSS_SELECTOR, "input[name='telephone']"))

    @property
    def password(self):
        return self.get_element((By.CSS_SELECTOR, "input[name='password']"))

    @property
    def confirm_password(self):
        return self.get_element((By.CSS_SELECTOR, "input[name='confirm']"))

    @property
    def continue_button(self):
        return self.get_element((By.CSS_SELECTOR, "input[type='submit']"))

    @property
    def agree_privacy_policy(self):
        return self.get_element((By.CSS_SELECTOR, "input[type='checkbox']"))

    def fill_user_data(self, first_name, last_name, email, telephone, password):
        self.set_text(self.first_name, first_name)
        self.set_text(self.last_name, last_name)
        self.set_text(self.email, email)
        self.set_text(self.telephone, telephone)
        self.set_text(self.password, password)
        self.set_text(self.confirm_password, password)
        self.mouse_click_to_element(self.agree_privacy_policy)
        self.mouse_click_to_element(self.continue_button)
