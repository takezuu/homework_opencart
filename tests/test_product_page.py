from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

URL = 'desktops/test'


class Page:
    LIKE_BUTTON = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    COMPARE_BUTTON = (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")
    IMAGE = (By.CSS_SELECTOR, ".image-additional > a > img")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    UPLOAD_FILE_BUTTON = (By.CSS_SELECTOR, "#button-upload222")


def test_like_button(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(Page.LIKE_BUTTON))
    except TimeoutException:
        raise AssertionError("Не дождалcя возможности клика по кнопке Like")


def test_compare_button(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(Page.COMPARE_BUTTON))
    except TimeoutException:
        raise AssertionError("Не дождалcя возможности клика по кнопке Cравнения товаров")


def test_pc_button_clickable(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(Page.ADD_TO_CART_BUTTON))
    except TimeoutException:
        raise AssertionError("Не дождалcя возможности клика по кнопке добавить в корзину")


def test_image(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(Page.IMAGE))
    except TimeoutException:
        raise AssertionError("Не присутствия на странице изображения")


def test_upload_button(browser, base_url):
    try:
        browser.get(base_url + URL)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(Page.UPLOAD_FILE_BUTTON))
    except TimeoutException:
        raise AssertionError("Не дождалcя на странице видимости кнопки Загрузить файл")
