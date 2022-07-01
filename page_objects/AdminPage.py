from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AdminPage(BasePage):
    PATH = 'admin'
    CLICKABLE_ELEMENT = LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    VISIBILITY_ELEMENTS = (By.CSS_SELECTOR, ".panel.panel-default")
    PRESENCE_ELEMENT = (By.CSS_SELECTOR, "#footer a")
    VISIBILITY_ELEMENT = LOGIN_FIELD = (By.CSS_SELECTOR, "#input-username")
    ELEMENT_ATTRIBUTE = PASSWORD_FIELD = ((By.CSS_SELECTOR, "#input-password"), 'type')
    LOGIN = 'user'
    PASSWORD = 'bitnami'
    product_name = 'Asus laptop'
    product_name_2 = 'Acer smart watch'
    meta_teg = 'Asus'
    product_model = 'X65C'

    def log_in(self, login, password):
        self.browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys(login)
        self.browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    def add_new_product(self, product_name, meta_teg, product_model):
        self.browser.find_element(By.CSS_SELECTOR, "#menu-catalog").click()
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-catalog > ul > "
                                                                                          "li:nth-child(2)"))).click()
        self.browser.find_element(By.CSS_SELECTOR, "[data-original-title='Add New']").click()
        self.browser.find_element(By.CSS_SELECTOR, "#input-name1").send_keys(product_name)
        self.browser.find_element(By.CSS_SELECTOR, "#input-meta-title1").send_keys(meta_teg)
        self.browser.find_element(By.CSS_SELECTOR, ".nav.nav-tabs > li:nth-child(2)").click()
        self.browser.find_element(By.CSS_SELECTOR, "#input-model").send_keys(product_model)
        self.browser.find_element(By.CSS_SELECTOR, "[data-original-title='Save']").click()

    def check_new_product(self, product_name):
        self.browser.find_element(By.CSS_SELECTOR, "#input-name").send_keys(product_name)
        self.browser.find_element(By.CSS_SELECTOR, "#button-filter").click()
        return self.browser.find_element(By.CSS_SELECTOR, "tbody tr .text-left").text

    def delete_product(self):
        self.browser.find_element(By.CSS_SELECTOR, "tbody .text-center input").click()
        self.browser.find_element(By.CSS_SELECTOR, "[data-original-title='Delete']").click()
        self.browser.switch_to.alert.accept()
        return self.browser.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
