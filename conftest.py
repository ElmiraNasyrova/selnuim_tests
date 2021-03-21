import pytest
import os

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default='chrome')
    parser.addoption("--browversion", action="store", default="88.0")
    parser.addoption("--executor", action="store", default="192.168.0.102")


@pytest.fixture
def browser(request):
    driver = None

    browser = request.config.getoption("--browser")
    version = request.config.getoption("--browversion")
    executor = request.config.getoption("--executor")

    add_environments_properties(browser, version)

    if browser.lower() != 'safari':
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

    elif browser == "safari":
        driver = webdriver.Safari()

    driver.maximize_window()

    def teardown():
        driver.quit()

    request.addfinalizer(teardown)

    return driver


def add_environments_properties(browser, version):
    with open('environment.properties', 'w') as f:
        f.write("Browser={browser}\n".format(browser = browser))
        f.write("Browser.Version={version}".format(version = version))

    folder_path = os.getcwd()
    os.replace("environment.properties", folder_path + "/allure-results/environment.properties")
