import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.opera import OperaDriverManager

DRIVER_PATH = "/Users/petro/Driver/"
OPERA_PATH = "/Users/petro/AppData/Local/Programs/Opera/86.0.4363.59/opera.exe"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", default="chrome", help="Choose browser"
    )
    parser.addoption(
        "--base_url", default="http://192.168.8.113:8081/"
    )


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service = Service(executable_path=DRIVER_PATH + "chromedriver.exe")
        browser = webdriver.Chrome(service=service)
        browser.maximize_window()
    elif browser_name == "firefox":
        service = Service(executable_path=DRIVER_PATH + "geckodriver.exe")
        browser = webdriver.Firefox(service=service)
        browser.maximize_window()
    elif browser_name == "opera":
        browser = webdriver.Opera(executable_path=OperaDriverManager().install())
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox or opera")
    yield browser
    browser.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")
