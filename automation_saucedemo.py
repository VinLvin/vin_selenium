import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.CLASS_NAME,"title").text
        response_message = browser.find_element(By.CLASS_NAME,"inventory_item_name").text

        self.assertIn('PRODUCTS', response_data)
        self.assertIn('Backpack', response_message)

    def test_a_failed_login_empty_password(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.CLASS_NAME,"error-message-container").text
        self.assertIn('Epic sadface: Password is required', response_data)

    def test_a_failed_login_empty_username(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"user-name").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.CLASS_NAME,"error-message-container").text
        self.assertIn('Epic sadface: Username is required', response_data)

    def test_a_success_logout(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.ID,"react-burger-menu-btn").click() #klik tombol burger menu
        time.sleep(1)
        browser.find_element(By.ID,"logout_sidebar_link").click() #klik tombol logout
        time.sleep(1)

        # validasi
        expected_url = "https://www.saucedemo.com/"
        self.assertEqual(expected_url,browser.current_url)

    def test_a_success_tentang(self):
            # steps
            browser = self.browser #buka web browser
            browser.get("https://www.saucedemo.com/") # buka situs
            time.sleep(2)
            browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
            time.sleep(1)
            browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
            time.sleep(1)
            browser.find_element(By.ID,"login-button").click() # klik tombol sign in
            time.sleep(1)
            browser.find_element(By.ID,"react-burger-menu-btn").click() #klik tombol burger menu
            time.sleep(1)
            browser.find_element(By.ID,"about_sidebar_link").click() #klik tombol logout
            time.sleep(1)

            # validasi
            expected_url = "https://saucelabs.com/"
            self.assertEqual(expected_url,browser.current_url)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
