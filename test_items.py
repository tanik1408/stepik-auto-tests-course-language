def test_button_add_product(browser, language_url):
    link = f"http://selenium1py.pythonanywhere.com/{language_url}/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert len(button) > 0, 'button not found'