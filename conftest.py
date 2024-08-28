import pytest
from selenium import webdriver

from data import ApiUrls


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(ApiUrls.HOME_URL)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(ApiUrls.HOME_URL)
    yield driver
    driver.quit()
