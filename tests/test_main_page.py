from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class Page:
    SHOPPING_BUTTON = (By.CSS_SELECTOR, "#cart > button")
    LOGO = (By.CSS_SELECTOR, "#logo > a > img")
    CURRENCY_BUTTON = (By.CSS_SELECTOR, ".btn-group > button")
    TOP_NAVBAR = (By.CSS_SELECTOR, ".collapse.navbar-collapse.navbar-ex1-collapse")
    CAROUSEL = (By.CSS_SELECTOR, "#carousel0")


def test_shopping_button(browser, base_url):
    try:
        browser.get(base_url)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Page.SHOPPING_BUTTON))
    except TimeoutException:
        raise AssertionError("Не дождалcя видимости кнопки с товарами на странице")


def test_logo(browser, base_url):
    try:
        browser.get(base_url)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Page.LOGO))
    except TimeoutException:
        raise AssertionError("Не дождалcя видимости доготипа на странице")


def test_currency_button(browser, base_url):
    try:
        browser.get(base_url)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Page.CURRENCY_BUTTON))
    except TimeoutException:
        raise AssertionError("Не дождалcя видимости кнопки с валютой на странице")


def test_top_navigation_bar(browser, base_url):
    try:
        browser.get(base_url)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Page.TOP_NAVBAR))
    except TimeoutException:
        raise AssertionError("Не дождалcя видимости навигационного бара на странице")


def test_carousel(browser, base_url):
    try:
        browser.get(base_url)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Page.CAROUSEL))
    except TimeoutException:
        raise AssertionError("Не дождалcя видимости карусели на странице")
