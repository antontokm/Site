from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture
def driver():
    s = Service('./Test/chromedriver.exe')
    web_driver = webdriver.Chrome(service = s)
    return web_driver