import os
import sys
sys.path.append(os.path.join(os.getcwd(), ""))
os.environ["DJANGO_SETTINGS_MODULE"] = "Site.settings"
import django
django.setup()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from page_objects.page_registration import PageRegistration
from page_objects.page_base import PageBase
from django.contrib.auth.models import User

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
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
