import os
import sys
sys.path.append(os.path.join(os.getcwd(), ""))
os.environ["DJANGO_SETTINGS_MODULE"] = "Site.settings"
import django
django.setup()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

import pytest

from django.contrib.auth.models import User

options_chrome = webdriver.ChromeOptions()
options_chrome.add_experimental_option('excludeSwitches', ['enable-logging'])

# options_firefox = webdriver.FirefoxOptions()
# options_firefox.add_experimental_option('excludeSwitches', ['enable-logging'])


@pytest.fixture(params=["Chrome", "Firefox"])
def driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    if request.param == "Firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()
    
@pytest.fixture
def chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('http://127.0.0.1:8000/')
    yield driver
    driver.quit()

@pytest.fixture
def firefox():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get('http://127.0.0.1:8000/')
    yield driver
    driver.quit()

@pytest.fixture
def get_site(driver):
    driver.get('http://127.0.0.1:8000/')

@pytest.fixture
def create_and_delete_user():
    User.objects.create_user("User_Test44444", email=None, password="1qaz@WSX3edc$RFV").save()
    yield
    User.objects.filter(username="User_Test44444").delete()
