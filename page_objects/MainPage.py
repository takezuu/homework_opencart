from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    CLICKABLE_ELEMENT = (By.CSS_SELECTOR, "#cart button")
    VISIBILITY_ELEMENTS = (By.CSS_SELECTOR, '.row')
    PRESENCE_ELEMENT = (By.CSS_SELECTOR, ".btn-group button")
    VISIBILITY_ELEMENT = (By.CSS_SELECTOR, ".collapse.navbar-collapse.navbar-ex1-collapse")
    ELEMENT_ATTRIBUTE = ((By.CSS_SELECTOR, ".swiper-container.swiper-container-horizontal"), 'id')

    def open_reg_form(self):
        self.browser.find_element(By.CSS_SELECTOR, ".dropdown").click()
        self.browser.find_element(By.CSS_SELECTOR, ".dropdown.open > ul > li > a").click()

    def define_currency(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".btn.btn-link.dropdown-toggle > strong").text

    def change_currency(self, currency):
        if currency == '$':
            self.browser.find_element(By.CSS_SELECTOR, ".btn-group").click()
            self.browser.find_element(By.CSS_SELECTOR, ".btn-group.open > ul > li > [name = 'EUR']").click()
        elif currency == '€':
            self.browser.find_element(By.CSS_SELECTOR, ".btn-group").click()
            self.browser.find_element(By.CSS_SELECTOR, ".btn-group.open > ul > li > [name='GBP']").click()
        elif currency == '£':
            self.browser.find_element(By.CSS_SELECTOR, ".btn-group").click()
            self.browser.find_element(By.CSS_SELECTOR, ".btn-group.open > ul > li > [name='USD']").click()
