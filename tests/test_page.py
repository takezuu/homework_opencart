from page_objects.MainPage import MainPage
from page_objects.AdminPage import AdminPage
from page_objects.CatalogPage import CatalogPage
from page_objects.ProductPage import ProductPage
from page_objects.UserRegistrationPage import UserRegistrationPage


def test_clickable_of_shopping_button(browser, base_url):
    MainPage(browser).open_url(base_url)
    MainPage(browser).check_clickable(MainPage.CLICKABLE_ELEMENT)


def test_of_all_elements_in_logo_row(browser, base_url):
    MainPage(browser).open_url(base_url)
    MainPage(browser).check_visibility_of_all_elements_located(MainPage.VISIBILITY_ELEMENTS)


def test_presence_of_currency_button(browser, base_url):
    MainPage(browser).open_url(base_url)
    MainPage(browser).check_presence_of_element(MainPage.PRESENCE_ELEMENT)


def test_visibility_of_top_navigation_bar(browser, base_url):
    MainPage(browser).open_url(base_url)
    MainPage(browser).check_visibility_of_element(MainPage.VISIBILITY_ELEMENT)


def test_carousel_for_element_attribute(browser, base_url):
    MainPage(browser).open_url(base_url)
    MainPage(browser).check_element_attribute(MainPage.ELEMENT_ATTRIBUTE)


def test_clickable_of_login_button(browser, base_url):
    AdminPage(browser).open_url(base_url, AdminPage.PATH)
    AdminPage(browser).check_clickable(AdminPage.CLICKABLE_ELEMENT)


def test_of_all_elements_login_panel(browser, base_url):
    AdminPage(browser).open_url(base_url, AdminPage.PATH)
    AdminPage(browser).check_visibility_of_all_elements_located(AdminPage.VISIBILITY_ELEMENTS)


def test_presence_of_open_cart_link(browser, base_url):
    AdminPage(browser).open_url(base_url, AdminPage.PATH)
    AdminPage(browser).check_presence_of_element(AdminPage.PRESENCE_ELEMENT)


def test_visibility_of_login_field(browser, base_url):
    AdminPage(browser).open_url(base_url, AdminPage.PATH)
    AdminPage(browser).check_visibility_of_element(AdminPage.VISIBILITY_ELEMENT)


def test_password_field_for_element_attribute(browser, base_url):
    AdminPage(browser).open_url(base_url, AdminPage.PATH)
    AdminPage(browser).check_element_attribute(AdminPage.ELEMENT_ATTRIBUTE)


def test_clickable_of_list_button(browser, base_url):
    CatalogPage(browser).open_url(base_url, CatalogPage.PATH)
    CatalogPage(browser).check_clickable(CatalogPage.CLICKABLE_ELEMENT)


def test_content_visibility_of_all_elements(browser, base_url):
    CatalogPage(browser).open_url(base_url, CatalogPage.PATH)
    CatalogPage(browser).check_visibility_of_all_elements_located(CatalogPage.VISIBILITY_ELEMENTS)


def test_presence_of_footer(browser, base_url):
    CatalogPage(browser).open_url(base_url, CatalogPage.PATH)
    CatalogPage(browser).check_presence_of_element(CatalogPage.PRESENCE_ELEMENT)


def test_visibility_of_left_column(browser, base_url):
    CatalogPage(browser).open_url(base_url, CatalogPage.PATH)
    CatalogPage(browser).check_visibility_of_element(CatalogPage.VISIBILITY_ELEMENT)


def test_computer_icon_for_element_attribute(browser, base_url):
    CatalogPage(browser).open_url(base_url, CatalogPage.PATH)
    CatalogPage(browser).check_element_attribute(CatalogPage.ELEMENT_ATTRIBUTE)


def test_clickable_of_like_button(browser, base_url):
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_clickable(ProductPage.CLICKABLE_ELEMENT)


def test_right_sidebar_visibility_of_all_elements(browser, base_url):
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_visibility_of_all_elements_located(ProductPage.VISIBILITY_ELEMENTS)


def test_presence_of_image(browser, base_url):
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_presence_of_element(ProductPage.PRESENCE_ELEMENT)


def test_visibility_of_add_to_cart_button(browser, base_url):
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_visibility_of_element(ProductPage.VISIBILITY_ELEMENT)


def test_upload_file_button_for_element_attribute(browser, base_url):
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_element_attribute(ProductPage.ELEMENT_ATTRIBUTE)


def test_clickable_of_continue_button(browser, base_url):
    UserRegistrationPage(browser).open_url(base_url, UserRegistrationPage.PATH)
    UserRegistrationPage(browser).check_clickable(UserRegistrationPage.CLICKABLE_ELEMENT)


def test_account_section_visibility_of_all_elements(browser, base_url):
    UserRegistrationPage(browser).open_url(base_url, UserRegistrationPage.PATH)
    UserRegistrationPage(browser).check_visibility_of_all_elements_located(UserRegistrationPage.VISIBILITY_ELEMENTS)


def test_presence_of_login_page_link(browser, base_url):
    UserRegistrationPage(browser).open_url(base_url, UserRegistrationPage.PATH)
    UserRegistrationPage(browser).check_presence_of_element(UserRegistrationPage.PRESENCE_ELEMENT)


def test_visibility_of_agree_check_box(browser, base_url):
    UserRegistrationPage(browser).open_url(base_url, UserRegistrationPage.PATH)
    UserRegistrationPage(browser).check_visibility_of_element(UserRegistrationPage.VISIBILITY_ELEMENT)


def test_right_column_for_element_attribute(browser, base_url):
    UserRegistrationPage(browser).open_url(base_url, UserRegistrationPage.PATH)
    UserRegistrationPage(browser).check_element_attribute(UserRegistrationPage.ELEMENT_ATTRIBUTE)


def test_registration_of_new_user(browser, base_url):
    MainPage(browser).open_url(base_url)
    MainPage(browser).open_reg_form()
    form_text = UserRegistrationPage(browser).fill_form(UserRegistrationPage.data)
    assert form_text == 'Your Account Has Been Created!', 'Аккаунт не зарегистрирован'


def test_change_currency(browser, base_url):
    MainPage(browser).open_url(base_url)
    currency = MainPage(browser).define_currency()
    MainPage(browser).change_currency(currency)
    currency_2 = MainPage(browser).define_currency()
    assert currency != currency_2, 'Валюта не переключилась'


def test_add_new_product_admin_panel(browser, base_url):
    AdminPage(browser).open_url(base_url, AdminPage.PATH)
    AdminPage(browser).log_in(AdminPage.LOGIN, AdminPage.PASSWORD)
    AdminPage(browser).add_new_product(AdminPage.product_name, AdminPage.meta_teg, AdminPage.product_model)
    product_name = AdminPage(browser).check_new_product(AdminPage.product_name)
    assert product_name == AdminPage.product_name, 'Продукт не добавлен'


def test_delete_product_admin_panel(browser, base_url):
    AdminPage(browser).open_url(base_url, AdminPage.PATH)
    AdminPage(browser).log_in(AdminPage.LOGIN, AdminPage.PASSWORD)
    AdminPage(browser).add_new_product(AdminPage.product_name_2, AdminPage.meta_teg, AdminPage.product_model)
    AdminPage(browser).check_new_product(AdminPage.product_name)
    delete_text = AdminPage(browser).delete_product()
    assert delete_text == 'Success: You have modified products!\n×', 'Товар не удален'
