import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, InvalidArgumentException
import allure


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.browser.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.handlers[:] = [file_handler]
        self.logger.setLevel(level=self.browser.log_level)

    def open_url(self, base_url, path=''):
        try:
            self.logger.info(f"Открываю url {base_url}")
            self.browser.get(base_url + path)
        except InvalidArgumentException:
            self.logger.error(f"Браузер не смог открыть url: {base_url}")

    def check_clickable(self, clickable_element):
        try:
            self.logger.info(f"Кликаю по элементу {clickable_element}")
            WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(clickable_element))
        except TimeoutException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='clickable_element')
            self.logger.error(f"Браузер не видит кликабельного элемента {clickable_element}")
            raise AssertionError("Не дождалcя возможности клика по кнопке")

    def check_visibility_of_all_elements_located(self, visibility_elements):
        try:
            self.logger.info(f"Проверяю видимость всех элементов в {visibility_elements}")
            WebDriverWait(self.browser, 5).until(EC.visibility_of_all_elements_located(visibility_elements))
        except TimeoutException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='visibility_of_all_elements')
            self.logger.error(f"Браузер не видит элементов {visibility_elements}")
            raise AssertionError("Не дождалcя видимости элемента")

    def check_presence_of_element(self, presence_element):
        try:
            self.logger.info(f"Проверяю наличие элемента расположенного по {presence_element}")
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(presence_element))
        except TimeoutException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='presence_of_element_located')
            self.logger.error(f"Браузер не видит пресутсвия элемента  {presence_element}")
            raise AssertionError("Не дождалcя присутствия элемента на странице")

    def check_visibility_of_element(self, visibility_element):
        try:
            self.logger.info(f"Проверяю видимость элемента {visibility_element}")
            WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(visibility_element))
        except TimeoutException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='visibility_element')
            self.logger.error(f"Браузер не видит расположенного элемента {visibility_element}")
            raise AssertionError("Не дождалcя видимости элемента на странице")

    def check_element_attribute(self, element_attribute):
        try:
            self.logger.info(f"Проверяю атрибут у элемента {element_attribute}")
            WebDriverWait(self.browser, 5).until(EC.element_attribute_to_include(*element_attribute))
        except TimeoutException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='element_attribute')
            self.logger.error(f"Браузер не нашел элемента с атрибутом {element_attribute}")
            raise AssertionError("Отсутствует атрибут")
