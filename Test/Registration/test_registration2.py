from elems import PageBase, PageRegistration
import random
# from django.contrib.auth.models import User



def test_smoke_registration(driver):
    i=random.random()
    driver.get('http://127.0.0.1:8000/')

    page_base = PageBase(driver)
    page_base.click_registration(driver)

    page_registaration = PageRegistration(driver)
    page_registaration.enter_username(driver, f"User_Test{i}")
    page_registaration.enter_password(driver, "1qaz@WSX3edc$RFV")
    page_registaration.enter_password_confirmation(driver, "1qaz@WSX3edc$RFV")
    page_registaration.click_button_submit(driver)

    assert page_registaration.return_username(driver).text == f"Hello, User_Test{i}."
#    print(User.objects.filter(username=f"User_Test{i}"))

def test_negativ_password_length(driver):
    i=random.random()
    driver.get('http://127.0.0.1:8000/')

    page_base = PageBase(driver)
    page_base.click_registration(driver)

    page_registaration = PageRegistration(driver)
    page_registaration.enter_username(driver, f"User_Test{i}")
    page_registaration.enter_password(driver, "qweAS1@")
    page_registaration.enter_password_confirmation(driver, "qweAS1@")
    page_registaration.click_button_submit(driver)

    assert page_registaration.return_text_description(driver).text == "This password is too short. It must contain at least 8 characters."

