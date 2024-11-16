import pytest

from page_objects.page_base import PageBase
from page_objects.page_authorization import PageAuthorization


@pytest.mark.smoke
def test_successful_authorization(driver, get_site, create_and_delete_user):
    page_base = PageBase(driver)
    page_base.click_log(driver)

    page_authorization = PageAuthorization(driver)
    page_authorization.enter_username(driver, "User_Test44444")
    page_authorization.enter_password(driver, "1qaz@WSX3edc$RFV")
    page_authorization.click_button_submit(driver)

    assert page_base.return_username(driver).text == "Hello, User_Test44444."