import datetime
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser_name", default="chrome", help="Choose browser")
    parser.addoption("--base_url", default="http://192.168.8.113:8081/")
    parser.addoption("--log_level", default="DEBUG")
    parser.addoption("--executor", default="192.168.56.1")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--bv")



@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Тест {} начался {}".format(request.node.name, datetime.datetime.now()))

    
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
    elif browser_name == "firefox":
        options  = webdriver.FirefoxOptions()
    elif browser_name == "opera":
        options  = webdriver.OperaOptions()
        options.add_experimental_option('w3c', True)
    else:
        logger.critical(f"Браузер: {browser_name} не запустился")
        raise pytest.UsageError("--browser_name должен быть chrome, firefox или opera")

    logger.info(f"Открываю браузер: {browser_name}")
    
    browser = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                               desired_capabilities={
                               "BrowserName": browser_name,
                               "browserVersion": version,
                               "selenoid:options": {
                               "enableVNC": vnc
                               }
                               },
                               options=options
                               )

    browser.log_level = log_level
    browser.logger = logger
    browser.test_name = request.node.name

    logger.info(f"Браузер:{browser}")

    yield browser
    browser.quit()

    logger.info("===> Тест {} закончился {}".format(request.node.name, datetime.datetime.now()))


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")
