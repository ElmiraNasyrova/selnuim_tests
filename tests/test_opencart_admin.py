import allure
from pages import AdminPage

USERNAME = 'user'
PASSWORD = 'bitnami'


@allure.description("Авторизация по уч записью админа, выход из уч записи")
def test_login_and_logout_admin(browser):
    admin_page = AdminPage(browser)

    admin_page.open()
    admin_page.login(USERNAME, PASSWORD)
    admin_page.logout()

    assert admin_page.login_button, "Не удалось разлогиниться"


@allure.title("Проверка отображения секций с товарами")
def test_check_product_section(browser):
    admin_page = AdminPage(browser)

    admin_page.open()
    admin_page.login(USERNAME, PASSWORD)
    admin_page.open_products()

    assert admin_page.table
