from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

URL = 'desktops'


class Page:
    COMPUTER_ICON = (By.CSS_SELECTOR, "#content > div > div > img")
    LEFT_COLUMN = (By.CSS_SELECTOR, "#column-left")
    LIST_VIEW = (By.CSS_SELECTOR, "#list-view")
    PC_BUTTON = (By.CSS_SELECTOR, ".list-group > a:nth-child(2)")
    CONTENT = (By.CSS_SELECTOR, "#content")


def test_list_button_clickable(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(Page.LIST_VIEW))
    except TimeoutException:
        raise AssertionError("Не дождалcя возможности клика по кнопке отображать как список")


def test_pc_button_clickable(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(Page.PC_BUTTON))
    except TimeoutException:
        raise AssertionError("Не дождалcя возможности клика по меню PC")


def test_content_on_page(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(Page.CONTENT))
    except TimeoutException:
        raise AssertionError("Не дождалcя наличия контента на странице")


def test_left_column(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(Page.LEFT_COLUMN))
    except TimeoutException:
        raise AssertionError("Не дождалcя наличия левого сайдбара на странице")


def test_computer_icon(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(Page.COMPUTER_ICON))
    except TimeoutException:
        raise AssertionError("Не дождалcя наличия иконки пк")
