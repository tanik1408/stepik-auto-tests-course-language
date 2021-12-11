from selenium.webdriver.common.by import By

def test_button_add_product_is_displayed(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR,".btn-add-to-basket")
    assert len(button) > 0, 'button not found'