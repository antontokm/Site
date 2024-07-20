from selenium.webdriver.common.by import By
from .page_base import PageBase


class PageRegistration(PageBase):
    def click_button_submit(self, driver):
        self.button_submit = driver.find_element(By.NAME,"submit")
        self.button_submit.click()
        
    def enter_username(self, driver, username):
        self.input_username = driver.find_element(By.NAME,"username")
        self.input_username.send_keys(username)

    def enter_password(self, driver, password):
        self.input_password = driver.find_element(By.NAME,"password1")
        self.input_password.send_keys(password)
    
    def enter_password_confirmation(self, driver, password_confirmation):
        self.input_password_confirmation = driver.find_element(By.NAME,"password2")
        self.input_password_confirmation.send_keys(password_confirmation)
    
    def return_text_description(self, driver):
        self.text_description = driver.find_element(By.XPATH,"/html/body/form/ul[2]/li")
        return self.text_description