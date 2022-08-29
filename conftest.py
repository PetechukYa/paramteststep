import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print("\nStart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    sleep(3)
    print("\nQuit browser..")
    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action='store',
        default="en-gb",
        help="Choose lang en-gb or uk "
    )


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("--language")
    return language

