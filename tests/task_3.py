from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

USERNAME = 'user'
PASSWORD = 'bitnami'


def auth_admin(admin_page):
    admin_page.find_element_by_name("username").send_keys(USERNAME)
    admin_page.find_element_by_name("password").send_keys(PASSWORD)
    admin_page.find_element_by_xpath("//*[@type='submit']").click()


def test_login_and_logout_admin(admin_page):
    auth_admin(admin_page)

    try:
        logout_button = WebDriverWait(admin_page, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'sign-out')]")))
        logout_button.click()
        result = True
    except TimeoutException:
        result = False

    assert result, "Не удалось залогиниться"

    login_button = admin_page.find_elements_by_xpath("//*[@type='submit']")
    assert len(login_button) == 1, "Не удалось разлогиниться"


def test_check_product_section(admin_page):
    auth_admin(admin_page)

    wait = WebDriverWait(admin_page, 10, 1)

    products_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#menu-catalog")))
    products_button.click()

    products_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='menu-catalog']//*[contains(text(), 'Products')]")))
    products_button.click()

    result = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table")))
    assert result is not []
