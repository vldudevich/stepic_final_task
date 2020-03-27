import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language_name', action='store', default="en",
                     help="Choose language: en or ru ")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language_name = request.config.getoption("language_name")
    browser = None

    if language_name == "en":
        print("\nchosen en for test..")
    elif language_name == "ru":
        print("\nchosen ru for test..")
    else:
        raise pytest.UsageError("--language_name should be ru or en")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")

        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
        
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")

        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language_name)

        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()