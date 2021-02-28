import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser",
                     default='chrome',
                     choices=["chrome", "firefox", "safari"],
                     help="Choice browser")
    parser.addoption("--headless",
                     action="store_true",
                     help="Run headless")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    driver = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless: options.headless = True
        driver = webdriver.Chrome(
            executable_path='//Users//finomteam//Desktop//Drivers//chromedriver',
            options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless: options.headless = True
        driver = webdriver.Firefox(
            executable_path='//Users//finomteam//Desktop//Drivers//geckodriver',
            options=options)

    elif browser == "safari":
        driver = webdriver.Safari()

    else:
        raise Exception("Specified wrong browser platform. Available platforms: [chrome, firefox, safari]")

    driver.maximize_window()

    def teardown():
        driver.quit()

    request.addfinalizer(teardown)

    return driver



@pytest.fixture(name='sign_in_page')
def open_sign_in_page(request, browser):
    base_url = request.config.getoption("--url")
    browser.get(base_url + '/index.php?route=account/login')
    return browser
