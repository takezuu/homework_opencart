from page_objects.ProductPage import ProductPage


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
