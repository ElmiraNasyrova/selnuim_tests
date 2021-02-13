from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_opencart_page(home_page):
    assert home_page.find_elements_by_css_selector("#logo") != []


def test_find_elements_in_home_page(home_page):
    home_page.find_element_by_css_selector("#cart-total")
    home_page.find_element_by_name("search")
    home_page.find_element_by_class_name('navbar')
    home_page.find_element_by_xpath("//*[@title='Checkout']")
    home_page.find_element_by_partial_link_text('Store')


def test_find_elements_in_components_catalog(catalog_page):
    wait = WebDriverWait(catalog_page, 5)

    wait.until(lambda driver: driver.find_element_by_link_text("Tablets"))
    wait.until(EC.visibility_of_element_located((By.ID, "input-sort")))

    catalog_page.find_element_by_xpath("//*[contains(text(),'Apple')]")
    catalog_page.find_element_by_partial_link_text("Components").click()
    catalog_page.find_element_by_partial_link_text("Printer").click()


def test_find_elements_in_product_card(product_card_page):
    wait = WebDriverWait(product_card_page, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "button-cart")))

    product_card_page.find_element_by_class_name('thumbnail')
    product_card_page.find_element_by_link_text("Description")
    product_card_page.find_element_by_name("quantity")
    product_card_page.find_element_by_xpath("//*[@id='content']//h1")


def test_find_elements_in_sign_in(sign_in_page):
    sign_in_page.find_element_by_name("email")
    sign_in_page.find_element_by_css_selector("#input-password")
    sign_in_page.find_element_by_xpath("//*[@type='submit']")
    sign_in_page.find_element_by_xpath("//*[@class='well']//*[contains(@href, 'register')]")
    sign_in_page.find_element_by_link_text("Register")


def test_find_elements_in_admin_login(admin_page):
    wait = WebDriverWait(admin_page, 10, 1)
    wait.until(EC.title_is("Administration"))

    admin_page.find_element_by_xpath("//*[@title='OpenCart']")
    admin_page.find_element_by_name("username")
    admin_page.find_element_by_id("input-password")
    admin_page.find_element_by_class_name('help-block')
    admin_page.find_element_by_css_selector("button[type='submit']")
