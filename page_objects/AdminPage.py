from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class AdminPage(BasePage):
    PATH = 'admin'
    CLICKABLE_ELEMENT = LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='submit1']")
    VISIBILITY_ELEMENTS = (By.CSS_SELECTOR, ".panel.panel-default1")
    PRESENCE_ELEMENT = (By.CSS_SELECTOR, "#footer a1")
    VISIBILITY_ELEMENT = LOGIN_FIELD = (By.CSS_SELECTOR, "#input-username1")
    ELEMENT_ATTRIBUTE = PASSWORD_FIELD = ((By.CSS_SELECTOR, "#input-password1"), 'type')
    LOGIN = 'user'
    PASSWORD = 'bitnami'
    product_name = 'Asus laptop'
    product_name_2 = 'Acer smart watch'
    meta_teg = 'Asus'
    product_model = 'X65C'

    @allure.step('Log in')
    def log_in(self, login, password):
        try:
            self.logger.info("Ввожу имя пользователя")
            self.browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys(login)
            self.logger.info("Ввожу пароль пользователя")
            self.browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys(password)
            self.logger.info("Нажимаю кнопку войти")
            self.browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='log_in')
            self.logger.error("Не залогинился")

    @allure.step('Add new product')
    def add_new_product(self, product_name, meta_teg, product_model):
        try:
            self.logger.info("Открываю каталог в меню")
            self.browser.find_element(By.CSS_SELECTOR, "#menu-catalog").click()
            self.logger.info("Открываю под категорию в каталоге меню")
            WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-catalog > ul > "
                                                                                              "li:nth-child(2)"))).click()
            self.logger.info("Нажимаю добавить новый товар")
            self.browser.find_element(By.CSS_SELECTOR, "[data-original-title='Add New']").click()
            self.logger.info("Ввожу название продукта")
            self.browser.find_element(By.CSS_SELECTOR, "#input-name1").send_keys(product_name)
            self.logger.info("Ввожу метатег")
            self.browser.find_element(By.CSS_SELECTOR, "#input-meta-title1").send_keys(meta_teg)
            self.logger.info("Переключаюсь на следующую вкладку нового товара")
            self.browser.find_element(By.CSS_SELECTOR, ".nav.nav-tabs > li:nth-child(2)").click()
            self.logger.info("Ввожу модель продукта")
            self.browser.find_element(By.CSS_SELECTOR, "#input-model").send_keys(product_model)
            self.logger.info("Сохраняю новый продукт")
            self.browser.find_element(By.CSS_SELECTOR, "[data-original-title='Save']").click()
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='add_new_product')
            self.logger.error("Новый продукт не добавлен")

    @allure.step('Check new product')
    def check_new_product(self, product_name):
        try:
            self.logger.info("Ввожу название продукта в поисковый фильтр")
            self.browser.find_element(By.CSS_SELECTOR, "#input-name").send_keys(product_name)
            self.logger.info("Нажимаю кнопку искать")
            self.browser.find_element(By.CSS_SELECTOR, "#button-filter").click()
            self.logger.info("Проверяю наличие продукта на страницу после поиска")
            return self.browser.find_element(By.CSS_SELECTOR, "tbody tr .text-left").text
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='check_new_product')
            self.logger.error("Проверка наличия нового продукта не удалась")

    @allure.step('Delete product')
    def delete_product(self):
        try:
            self.logger.info("Нажимаю на чекбокс удаляемого продукта")
            self.browser.find_element(By.CSS_SELECTOR, "tbody .text-center input").click()
            self.logger.info("Нажимаю на кнопку удаления продукта")
            self.browser.find_element(By.CSS_SELECTOR, "[data-original-title='Delete']").click()
            self.logger.info("Подтверждаю аллерт")
            self.browser.switch_to.alert.accept()
            return self.browser.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='delete_product')
            self.logger.error("Товар не удален")
