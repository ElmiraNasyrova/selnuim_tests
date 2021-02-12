from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

USERNAME = 'demo'
PASSWORD = 'demo'


def auth_admin(browser):
    browser.get("https://demo.opencart.com/admin/")

    browser.find_element_by_name("username").clear()
    browser.find_element_by_name("password").clear()

    browser.find_element_by_name("username").send_keys(USERNAME)
    browser.find_element_by_name("password").send_keys(PASSWORD)
    browser.find_element_by_xpath("//*[@type='submit']").click()


def test_login_and_logout_admin(browser):
    auth_admin(browser)

    try:
        logout_button = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'sign-out')]")))
        logout_button.click()
        result = True
    except TimeoutException:
        result = False

    assert result, "Не удалось залогиниться"

    login_button = browser.find_elements_by_xpath("//*[@type='submit']")
    assert len(login_button) == 1, "Не удалось разлогиниться"


def test_check_product_section(browser):
    auth_admin(browser)

    wait = WebDriverWait(browser, 10, 1)

    products_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#menu-catalog")))
    products_button.click()

    products_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='menu-catalog']//*[contains(text(), 'Products')]")))
    products_button.click()

    result = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table")))
    assert result is not []
