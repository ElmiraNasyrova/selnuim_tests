from pages import HomePage, NavigationBar, CategoriesPage, ProductPage, SignUpPage, SignInPage
from pages.common import TopMenu, Alert
from mimesis import Person


def test_open_opencart_page(browser):
    home_page = HomePage(browser)
    home_page.open_page()
    assert home_page.opencart_logo


def test_add_featured_product_to_cart_from_home_page(browser):
    home_page = HomePage(browser)
    home_page.open_page()

    product_name = home_page.get_featured_product_name_by_index(0)
    home_page.add_to_cart_featured_product(0)

    top_menu = TopMenu(browser)
    top_menu.click_to_cart()
    added_product_name = top_menu.get_added_product_name()

    assert product_name in added_product_name


def test_open_product_card_from_catalog(browser):
    CATEGORY = 'Tablets'

    category_page =CategoriesPage(browser)
    category_page.open()

    NavigationBar(browser).open_page()
    NavigationBar(browser).open_section_by_name(CATEGORY)

    section_title = category_page.get_category_name()
    assert section_title == CATEGORY

    product_name = category_page.get_product_name_in_minicard()
    print("product_name", product_name)
    category_page.open_product_card()

    product_title = ProductPage(browser).get_product_name()
    assert product_title == product_name


def test_add_product_to_cart_from_product_page(browser):
    QTY = 2

    product_page = ProductPage(browser)
    product_page.open()
    product_price = product_page.get_product_price()
    product_page.set_quantity(QTY)
    product_page.add_to_cart()

    assert Alert(browser).alert

    top_menu = TopMenu(browser)
    cart_total_amount = top_menu.get_cart_text()

    product_price = float(product_price.replace("$", ""))

    assert str(product_price*QTY) in cart_total_amount


def test_sign_up_user(browser):
    person = Person()
    TEST_DATA = {
        'first_name': person.first_name(),
        'last_name': person.last_name(),
        'email': person.email(),
        'telephone': person.telephone(),
        'password': person.password(8)
    }

    sign_up_page = SignUpPage(browser)
    sign_up_page.open()
    sign_up_page.fill_user_data(
        first_name=TEST_DATA['first_name'],
        last_name=TEST_DATA['last_name'],
        email=TEST_DATA['email'],
        telephone=TEST_DATA['telephone'],
        password=TEST_DATA['password']
    )
    TopMenu(browser).logout()

    sign_in_page = SignInPage(browser)
    sign_in_page.confirm_logout()
    sign_in_page.open()
    sign_in_page.login(TEST_DATA['email'], TEST_DATA['password'])

    assert sign_in_page.get_available_actions_header() == 'My Account'
