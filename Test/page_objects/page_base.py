from selenium.webdriver.common.by import By

class PageBase():
    def __init__(self, driver):
        self.driver = driver
    
    def click_registration(self, driver):
        self.registration = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]")
        self.registration.click()
    
    def click_log(self, driver):
        self.log = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]")
        self.log.click()
    
    def click_main_page(self, driver):
        self.main_page = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/a")
        self.main_page.click()
    
    def click_forum(self, driver):
        self.forum = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/a")
        self.forum.click()
    
    def return_username(self, driver):
        self.username = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]")
        return self.username