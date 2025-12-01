import pytest
from selene import browser


@pytest.fixture(autouse=True)
def settings_browser():
    browser.config.driver_name = 'firefox'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10
    browser.config.headless = False

    yield

    browser.quit()