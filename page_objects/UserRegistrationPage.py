from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class UserRegistrationPage(BasePage):
    PATH = 'index.php?route=account/register'
    CLICKABLE_ELEMENT = (By.CSS_SELECTOR, "[value='Continue']")
    VISIBILITY_ELEMENTS = (By.CSS_SELECTOR, "#account")
    PRESENCE_ELEMENT = (By.CSS_SELECTOR, "#content p a")
    VISIBILITY_ELEMENT = (By.CSS_SELECTOR, "[name='agree']")
    ELEMENT_ATTRIBUTE = ((By.CSS_SELECTOR, "#column-right"), 'class')
    reg_data = ['Alex21', 'Newton23', '23myemail@mail.mail', '+83467564732', 'CoolPassword123']
    reg_selectors = ["#input-firstname", "#input-lastname", "#input-email", "#input-telephone", "#input-password"]
    data = dict(zip(reg_selectors, reg_data))

    def fill_form(self, data):
        for k, v in data.items():
            self.browser.find_element(By.CSS_SELECTOR, f"{k}").send_keys(f"{v}")
            if k == "#input-password":
                password = v
        self.browser.find_element(By.CSS_SELECTOR, "#input-confirm").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "[name='agree']").click()
        self.browser.find_element(By.CSS_SELECTOR, "[value='Continue']").click()
        return self.browser.find_element(By.CSS_SELECTOR, "#content h1").text
