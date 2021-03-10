from pages import AdminPage

import time

USERNAME = 'user'
PASSWORD = 'bitnami'


def test_login_and_logout_admin(browser):
    admin_page = AdminPage(browser)

    admin_page.open()
    admin_page.login(USERNAME, PASSWORD)
    admin_page.logout()

    assert admin_page.login_button, "Не удалось разлогиниться"


def test_check_product_section(browser):
    admin_page = AdminPage(browser)

    admin_page.open()
    admin_page.login(USERNAME, PASSWORD)
    admin_page.open_products()

    assert admin_page.table
