import os
import sys
sys.path.append(os.path.join(os.getcwd(), ""))
os.environ["DJANGO_SETTINGS_MODULE"] = "Site.settings"
import django
django.setup()
import pytest

from page_objects.page_registration import PageRegistration
from page_objects.page_base import PageBase
import random
from django.contrib.auth.models import User


@pytest.mark.smoke
def test_successful_registration(driver, get_site):
    i=random.random()

    page_base = PageBase(driver)
    page_base.click_registration(driver)

    page_registaration = PageRegistration(driver)
    page_registaration.enter_username(driver, f"User_Test{i}")
    page_registaration.enter_password(driver, "1qaz@WSX3edc$RFV")
    page_registaration.enter_password_confirmation(driver, "1qaz@WSX3edc$RFV")
    page_registaration.click_button_submit(driver)

    assert page_registaration.return_username(driver).text == f"Hello, User_Test{i}."
    User.objects.filter(username=f"User_Test{i}").delete()

@pytest.mark.regression
def test_negativ_password_length_short(driver, get_site):
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
def test_negativ_password_commonly(driver, get_site):
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
def test_negativ_passwords_different(driver, get_site):
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
def test_negativ_password_similar_username(driver, get_site):
    page_base = PageBase(driver)
    page_base.click_registration(driver)

    page_registaration = PageRegistration(driver)
    page_registaration.enter_username(driver, f"User_Test123")
    page_registaration.enter_password(driver, "User_Test123@")
    page_registaration.enter_password_confirmation(driver, "User_Test123@")
    page_registaration.click_button_submit(driver)

    assert page_registaration.return_text_description(driver).text == "The password is too similar to the username."

@pytest.mark.regression
def test_negativ_password_only_numeric(driver, get_site):
    i=random.random()

    page_base = PageBase(driver)
    page_base.click_registration(driver)

    page_registaration = PageRegistration(driver)
    page_registaration.enter_username(driver, f"User_Test{i}")
    page_registaration.enter_password(driver, "87126534")
    page_registaration.enter_password_confirmation(driver, "87126534")
    page_registaration.click_button_submit(driver)

    assert page_registaration.return_text_description(driver).text == "This password is entirely numeric."