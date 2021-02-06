import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser",
                     default = 'safari',
                     choices=["chrome", "firefox", "safari"],
                     help="Choice browser")
    parser.addoption("--url",
                     default='http://localhost',
                     help="Input url")
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
            executable_path= '//Users//finomteam//Desktop//Drivers//geckodriver',
            options=options)

    elif browser == "safari":
        driver = webdriver.Safari()

    else:
        raise RuntimeError("Specified wrong browser platform. Available platforms: [chrome, firefox, safari]")

    driver.maximize_window()

    def teardown(): driver.close()
    request.addfinalizer(teardown)

    return driver


@pytest.fixture(scope='session', name='home_page')
def open_home_page(request, browser):
    url = request.config.getoption("--url")
    browser.get(url)

    return
