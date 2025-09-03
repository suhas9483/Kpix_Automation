import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages import Login_Unification_Page
from utilities.read_properties import Read_Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait





class Test_01_login_admin:

    driver = webdriver.Chrome()
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()


    def teardown_method(self):
        self.driver.quit()

    def test_title_verifictaion(self):
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "KpiX IoT Application"
        assert act_title == exp_title, f"Expected title '{exp_title}', got '{act_title}'"
        WebDriverWait(self.driver, 10).until(EC.title_contains("KpiX"))
    def test_valid_login(self):
        self.driver.get(self.admin_page_url)
        login = Login_Unification_Page(self.driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()
        dashboard_button_text = self.driver.find_element(By.XPATH, ).text
        assert dashboard_button_text == "button"
        WebDriverWait(self.driver, 10).until(EC.title_contains("KpiX"))
    def test_invalid_login(self):
        self.driver.get(self.admin_page_url)
        login = Login_Unification_Page(self.driver)
        login.enter_username(self.invalid_username)
        login.enter_password(self.password)
        login.click_login()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='root']/div/nav/div[1]").text
        assert error_message == "button"
        WebDriverWait(self.driver, 10).until(EC.title_contains("KpiX"))
