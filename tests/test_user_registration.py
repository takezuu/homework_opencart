from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

URL = 'index.php?route=account/register'


class Page:
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[value='Continue']")
    LOGIN_PAGE_LINK = (By.CSS_SELECTOR, "#content > p > a")
    AGREE_CHECKBOX = (By.CSS_SELECTOR, "[name='agree']")
    RIGHT_COLUMN = (By.CSS_SELECTOR, "#column-right")
    ACCOUNT_SECTION = (By.CSS_SELECTOR, "#account")


def test_continue_button(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(Page.CONTINUE_BUTTON))
    except TimeoutException:
        raise AssertionError("Не дождалcя возможности клика по кнопке Продолжить")


def test_login_page_link(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(Page.LOGIN_PAGE_LINK))
    except TimeoutException:
        raise AssertionError("Не дождалcя возможности клика по ссылке Страница авторизации")


def test_agree_check_box(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(Page.AGREE_CHECKBOX))
    except TimeoutException:
        raise AssertionError("Не дождалcя возможности клика по чекбокс Согласен")


def test_right_column(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(Page.RIGHT_COLUMN))
    except TimeoutException:
        raise AssertionError("Не дождалcя наличия правого сайдбара на странице")


def test_account_section(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(Page.ACCOUNT_SECTION))
    except TimeoutException:
        raise AssertionError("Не дождалcя наличия секции регистрации аккаунта на странице")
