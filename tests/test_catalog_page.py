from page_objects.CatalogPage import CatalogPage


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
