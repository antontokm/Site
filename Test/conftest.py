from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def driver():
    s = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    web_driver = webdriver.Chrome(service = s)
    return web_driver

@pytest.fixture
def get_site(driver):
    driver.get('http://127.0.0.1:8000/')