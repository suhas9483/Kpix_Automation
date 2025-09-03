from selenium.webdriver.common.by import By

class Login_Unification_Page:
    def __init__(self, driver,textbox_username_name,textbox_password_name,button_login_xpath):
        self.driver = driver
        self.textbox_username_name = "email"
        self.textbox_password_name = "password"
        self.button_login_xpath = "//*[@id='root']/div/div[1]/form/button"

    #// *[ @ id = "root"] / div / div[1] / form / button
    #// button[text() = 'Login']

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
