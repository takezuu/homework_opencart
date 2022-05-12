from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

URL = 'admin/'


class Page:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    HELP_BLOCK = (By.CSS_SELECTOR, ".help-block > a")
    FOOTER = (By.CSS_SELECTOR, "#footer > a")
    LOGIN_FIELD = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")


def test_login_button(browser, base_url):
    try:
        browser.get(base_url+URL)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(Page.LOGIN_BUTTON))
    except TimeoutException:
        raise AssertionError("Не дождалcя возможности клика по кнопке Логин")



def test_help_block(browser, base_url):
    try:
        browser.get(base_url+URL)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(Page.HELP_BLOCK))
    except TimeoutException:
        raise AssertionError("Не дождалcя возможности клика по кнопке Забыл пароль")


def test_pc_button_clickable(browser, base_url):
    try:
        browser.get(base_url+URL)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(Page.FOOTER))
    except TimeoutException:
        raise AssertionError("Не дождалcя возможности клика по футеру")


def test_login_field(browser, base_url):
    try:
        browser.get(base_url+URL)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(Page.LOGIN_FIELD))
    except TimeoutException:
        raise AssertionError("Не дождалcя наличия поля для логина на странице")


def test_password_field(browser, base_url):
    try:
        browser.get(base_url+URL)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(Page.PASSWORD_FIELD))
    except TimeoutException:
        raise AssertionError("Не дождалcя наличия поля для ввода пароля на странице")
