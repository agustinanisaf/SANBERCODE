import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRegister(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_success_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("agustin@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("passwordagustin") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "signin_login").click()
        time.sleep(2)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click() #klik tombol OK untuk menutup popup
        time.sleep(1)

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')
    
    def test_a_failed_login_with_empty_password(self): 
        # steps
        driver = self.browser #buka web browser
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("agustin@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # kosongi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(2)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click() #klik tombol OK untuk menutup popup
        time.sleep(1)

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_b_failed_login_with_empty_email(self): 
        # steps
        driver = self.browser #buka web browser
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # kosongi email
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("passwordagustin") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(2)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click() #klik tombol OK untuk menutup popup
        time.sleep(1)

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')
    
    def test_c_failed_login_with_empty_email_and_password(self): 
        # steps
        driver = self.browser #buka web browser
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # kosongi email
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # kosongi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(2)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click() #klik tombol OK untuk menutup popup
        time.sleep(1)

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__":
    unittest.main()