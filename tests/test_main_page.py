from page_objects.MainPage import MainPage


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


def test_change_currency(browser, base_url):
    MainPage(browser).open_url(base_url)
    currency = MainPage(browser).define_currency()
    MainPage(browser).change_currency(currency)
    currency_2 = MainPage(browser).define_currency()
    assert currency != currency_2, 'Валюта не переключилась'
