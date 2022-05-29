from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def open_url(self, base_url, path=''):
        self.browser.get(base_url + path)

    def check_clickable(self, clickable_element):
        try:
            WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(clickable_element))
        except TimeoutException:
            raise AssertionError("Не дождалcя возможности клика по кнопке")

    def check_visibility_of_all_elements_located(self, visibility_elements):
        try:
            WebDriverWait(self.browser, 5).until(EC.visibility_of_all_elements_located(visibility_elements))
        except TimeoutException:
            raise AssertionError("Не дождалcя видимости элемента'")

    def check_presence_of_element(self, presence_element):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(presence_element))
        except TimeoutException:
            raise AssertionError("Не дождалcя присутствия элемента на странице")

    def check_visibility_of_element(self, visibility_element):
        try:
            WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(visibility_element))
        except TimeoutException:
            raise AssertionError("Не дождалcя видимости элемента на странице")

    def check_element_attribute(self, element_attribute):
        try:
            WebDriverWait(self.browser, 5).until(EC.element_attribute_to_include(*element_attribute))
        except TimeoutException:
            raise AssertionError("Отсутствует атрибут")
