from selenium.webdriver.common.by import By
from .page_base import PageBase


class PageAuthorization(PageBase):
    def enter_username(self, driver, username):
        self.input_username = driver.find_element(By.NAME,"username")
        self.input_username.send_keys(username)
    
    def enter_password(self, driver, password):
        self.input_password = driver.find_element(By.NAME,"password")
        self.input_password.send_keys(password)
    
    def click_button_submit(self, driver):
        self.button_submit = driver.find_element(By.NAME,"submit")
        self.button_submit.click()