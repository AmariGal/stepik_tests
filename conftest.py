import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru or es")
					 
@pytest.fixture(scope="function")
def browser(request):
	lang = request.config.getoption('language')
	options = Options()
	options.add_experimental_option('prefs', {'intl.accept_languages': lang})
	print('\nstart Chrome browser...')
	browser = webdriver.Chrome(options=options)
	yield browser
	time.sleep(30)
	print('\nquit Chrome browser...')
	browser.quit()