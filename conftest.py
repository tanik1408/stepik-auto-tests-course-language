import pytest
from selenium import webdriver

language = None

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, es, fr and etc")

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser ..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture
def language_url(request):
    global language
    language = request.config.getoption("language")
    return language