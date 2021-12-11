def test_button_add_product(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert len(button) > 0, 'button not found'