from http import server
from importlib.resources import path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def driver():
    s = Service('./Test/chromedriver')
    web_driver = webdriver.Chrome(service = s)
    return web_driver

@pytest.fixture
def driver_login():
    s = Service('./Test/chromedriver')
    web_driver = webdriver.Chrome(service = s)
    log_in(web_driver)
    return web_driver

def test_log_in(driver):
    log_in(driver)
    elem_username = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]")
    assert elem_username.text == "Hello, User_Test1."

@pytest.mark.xfail
def test_registration(driver):
    i=1
    driver.get('http://127.0.0.1:8000/')

    elem_register = driver.find_element(By.CLASS_NAME,"header_usermenu_register")
    elem_register.click()

    elem_field_username = driver.find_element(By.NAME,"username")
    elem_field_username.send_keys(f"User_Test{i}")

    elem_field_password = driver.find_element(By.NAME,"password1")
    elem_field_password.send_keys("1qaz@WSX3edc$RFV")

    elem_field_password = driver.find_element(By.NAME,"password2")
    elem_field_password.send_keys("1qaz@WSX3edc$RFV")

    elem_button_submit = driver.find_element(By.NAME,"submit")
    elem_button_submit.click()

    elem_username = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]")
    assert elem_username.text == f"Hello, User_Test{i}."


def test_log_out(driver_login):
    log_out(driver_login)

    elem_register = driver_login.find_element(By.CLASS_NAME,"header_usermenu_register")
    assert elem_register.text == f"Register"


def test_write_comment(driver_login):
    elem_forum = driver_login.find_element(By.CLASS_NAME,"header_menu_forum")
    elem_forum.click()

    elem_field_comment = driver_login.find_element(By.NAME,"text")
    elem_field_comment.send_keys("Test")

    elem_button_submit = driver_login.find_element(By.NAME,"submit")
    elem_button_submit.click()

    elem_last_comment = driver_login.find_elements(By.CLASS_NAME,"forum_block_text")[-1]
    assert elem_last_comment.text == "Test"    


def log_in(driver):
    driver.get('http://127.0.0.1:8000/')

    elem_login = driver.find_element(By.CLASS_NAME,"header_usermenu_login")
    elem_login.click()

    elem_field_username = driver.find_element(By.NAME,"username")
    elem_field_username.send_keys("User_Test1")

    elem_field_password = driver.find_element(By.NAME,"password")
    elem_field_password.send_keys("1qaz@WSX3edc$RFV")

    elem_button_submit = driver.find_element(By.NAME,"submit")
    elem_button_submit.click()

def log_out(driver):
    elem_log_out = driver.find_element(By.CLASS_NAME,"header_usermenu_logout")
    elem_log_out.click()