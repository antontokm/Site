import os
import sys

from selenium.webdriver.chrome.webdriver import WebDriver
sys.path.append(os.path.join(os.getcwd(), ""))
os.environ["DJANGO_SETTINGS_MODULE"] = "Site.settings"
import django
django.setup()
import pytest
import allure

from page_objects.page_registration import PageRegistration
from page_objects.page_base import PageBase
import random
from django.contrib.auth.models import User


@pytest.mark.smoke
@allure.title("Проверка успешной регистрации")
@pytest.mark.parametrize("driver", ["Chrome"], indirect=True)
def test_successful_registration(driver: WebDriver, get_site: None):
    i=random.random()

    page_base = PageBase(driver)
    with allure.step("Открываем страницу регистрации"):
        page_base.click_registration(driver)

    page_registaration = PageRegistration(driver)
    with allure.step("Вводим значение в поле username"):
        page_registaration.enter_username(driver, f"User_Test{i}")
    with allure.step("Вводим значение в поле password"):
        page_registaration.enter_password(driver, "1qaz@WSX3edc$RFV")
    with allure.step("Вводим значение в поле password_confirmation"):
        page_registaration.enter_password_confirmation(driver, "1qaz@WSX3edc$RFV")
    with allure.step("Нажимаем на кнопку Submit"):
        page_registaration.click_button_submit(driver)

    with allure.step("Проверяме что регистрация прошла успешно"):
        assert page_registaration.return_username(driver).text == f"Hello, User_Test{i}."
    User.objects.filter(username=f"User_Test{i}").delete()

@pytest.mark.regression
@allure.title("Проверка регистрации с коротким паролем")
@pytest.mark.parametrize("driver", ["Chrome"], indirect=True)
def test_negativ_password_length_short(driver: WebDriver, get_site: None):
    i=random.random()

    page_base = PageBase(driver)
    page_base.click_registration(driver)

    page_registaration = PageRegistration(driver)
    page_registaration.enter_username(driver, f"User_Test{i}")
    page_registaration.enter_password(driver, "qweAS1@")
    page_registaration.enter_password_confirmation(driver, "qweAS1@")
    page_registaration.click_button_submit(driver)

    assert page_registaration.return_text_description(driver).text == "This password is too short. It must contain at least 8 characters."

@pytest.mark.regression
@allure.title("Проверка регистрации с обычным паролем")
@pytest.mark.parametrize("driver", ["Chrome"], indirect=True)
def test_negativ_password_commonly(driver: WebDriver, get_site: None):
    i=random.random()

    page_base = PageBase(driver)
    page_base.click_registration(driver)

    page_registaration = PageRegistration(driver)
    page_registaration.enter_username(driver, f"User_Test{i}")
    page_registaration.enter_password(driver, "qweASD123")
    page_registaration.enter_password_confirmation(driver, "qweASD123")
    page_registaration.click_button_submit(driver)

    assert page_registaration.return_text_description(driver).text == "This password is too common."

@pytest.mark.regression
@allure.title("Проверка регистрации с несовпадаюшими паролями")
@pytest.mark.parametrize("driver", ["Chrome"], indirect=True)
def test_negativ_passwords_different(driver: WebDriver, get_site: None):
    i=random.random()

    page_base = PageBase(driver)
    page_base.click_registration(driver)

    page_registaration = PageRegistration(driver)
    page_registaration.enter_username(driver, f"User_Test{i}")
    page_registaration.enter_password(driver, "qweASD123")
    page_registaration.enter_password_confirmation(driver, "qweASD123@")
    page_registaration.click_button_submit(driver)

    assert page_registaration.return_text_description(driver).text == "The two password fields didn’t match."

@pytest.mark.regression
@allure.title("Проверка регистрации с паролем содержищм данные из логина")
@pytest.mark.parametrize("driver", ["Chrome"], indirect=True)
def test_negativ_password_similar_username(driver: WebDriver, get_site):
    page_base = PageBase(driver)
    page_base.click_registration(driver)

    page_registaration = PageRegistration(driver)
    page_registaration.enter_username(driver, f"User_Test123")
    page_registaration.enter_password(driver, "User_Test123@")
    page_registaration.enter_password_confirmation(driver, "User_Test123@")
    page_registaration.click_button_submit(driver)

    assert page_registaration.return_text_description(driver).text == "The password is too similar to the username."

@pytest.mark.regression
@allure.title("Проверка регистрации с паролем содержищм только числа")
@pytest.mark.parametrize("driver", ["Chrome"], indirect=True)
def test_negativ_password_only_numeric(driver: WebDriver, get_site: None):
    i=random.random()

    page_base = PageBase(driver)
    page_base.click_registration(driver)

    page_registaration = PageRegistration(driver)
    page_registaration.enter_username(driver, f"User_Test{i}")
    page_registaration.enter_password(driver, "87126534")
    page_registaration.enter_password_confirmation(driver, "87126534")
    page_registaration.click_button_submit(driver)

    assert page_registaration.return_text_description(driver).text == "This password is entirely numeric."