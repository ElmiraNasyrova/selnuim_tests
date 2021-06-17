import logging
import os

import allure
import pytest
from selenium import webdriver

logging.basicConfig(level=logging.INFO, filename=os.getcwd() + "/selenium.log")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default='firefox')
    parser.addoption("--browversion", action="store", default="89.0")
    parser.addoption("--executor", action="store", default="192.168.0.100")
    parser.addoption("--localexecute", action="store", default=True)
    parser.addoption("--headless", action="store_true", help="Run headless")


@pytest.fixture
def browser(request):
    driver = None

    local = request.config.getoption("--localexecute")
    browser = request.config.getoption("--browser")
    version = request.config.getoption("--browversion")
    executor = request.config.getoption("--executor")
    headless = request.config.getoption("--headless")

    add_environments_properties(browser, version)

    if not local and browser.lower() != 'safari':
        executor_url = f"http://{executor}:4444/wd/hub"

        capabilities = {
            "browserName": browser,
            "version": version,
            "screenResolution": "1280x720",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False,
                "enableLog": False
            }
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=capabilities)

    elif local and browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless: options.headless = True
        driver = webdriver.Chrome(
            executable_path='//Users//finomteam//Desktop//Drivers//chromedriver',
            options=options)

    elif local and browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless: options.headless = True
        driver = webdriver.Firefox(
            executable_path='//Users//finomteam//Desktop//Drivers//geckodriver',
            options=options)

    elif browser == "safari":
        driver = webdriver.Safari()

    driver.maximize_window()

    def teardown():
        if request.node.rep_call.failed:
            allure.attach(
                body=driver.get_screenshot_as_png(),
                name=request.function.__name__,
                attachment_type=allure.attachment_type.PNG)

        driver.quit()

    request.addfinalizer(teardown)

    return driver


def add_environments_properties(browser, version):
    with open('environment.properties', 'w') as f:
        f.write("Browser={browser}\n".format(browser=browser))
        f.write("Browser.Version={version}".format(version=version))

    folder_path = os.getcwd()
    os.replace("environment.properties", folder_path + "/allure-results/environment.properties")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
