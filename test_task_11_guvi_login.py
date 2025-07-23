#importing the time module to set sleep time
import time

#importing the web drivers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
Login_name = "vnmmmagesh@gmail.com"
Login_Password = "Siddhu@oct10"
#function to test Guvi Login
def test_guvi_login_validation():
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://www.guvi.in/')
        time.sleep(3)
        driver.find_element(By.ID, "login-btn").click()
        time.sleep(3)

        #Validating the url
        curr_url = driver.current_url
        assert curr_url == "https://www.guvi.in/sign-in/", "Expected url not matching with current url"
        driver.maximize_window()
        time.sleep(2)

        #Getting information using locators
        verify_username = driver.find_element(By.ID, "email")
        user_password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-btn")

        #Validating login input boxes
        assert verify_username.is_displayed() and verify_username.is_enabled(), "Username not visible or enabled"
        assert user_password.is_displayed() and user_password.is_enabled(), "User Password not visible or enabled"
        assert login_button.is_displayed() and login_button.is_enabled(), "Login button not visible or enabled"

        #perform login using credentials
        verify_username.clear()
        verify_username.send_keys("vnmmagesh@gmail.com")


        user_password.clear()
        user_password.send_keys("Siddhu@oct10")

        current_username = verify_username.get_attribute("value")
        current_password = user_password.get_attribute("value")
        if current_username != Login_name:
                print("Username or Password not matching")
                driver.quit()
        if current_password != Login_Password:
                print("Password not matching")
                driver.quit()

        time.sleep(3)
        login_button.click()
        time.sleep(3)

        #Closing the browser
        driver.quit()