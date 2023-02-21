import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRegister(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_failed_register_with_email_registered(self):
        # steps
        driver = self.browser #buka web browser

        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(1)
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("agustin anisa") # isi nama
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("agustin@gmail.com") # isi email yang sudah didaftarkan
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("passwordagustin") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(1)
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click() #klik tombol OK untuk menutup popup
        time.sleep(1)

        # validasi
        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')
    
    def test_a_failed_register_with_empty_name(self):
        # steps
        driver = self.browser #buka web browser

        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("") # kosongi nama
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("agustin@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("passwordagustin") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(1)
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click() #klik tombol OK untuk menutup popup
        time.sleep(1)

        # validasi
        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def test_b_failed_register_with_empty_email(self):
        # steps
        driver = self.browser #buka web browser

        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("agustin anisa") # isi nama
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("") # kosongi email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("passwordagustin") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(1)
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click() #klik tombol OK untuk menutup popup
        time.sleep(1)

        # validasi
        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def test_c_failed_register_with_empty_password(self):
        # steps
        driver = self.browser #buka web browser

        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("agustin anisa") # isi nama
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("agustin@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("") # kosongi password
        time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(1)
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click() #klik tombol OK untuk menutup popup
        time.sleep(1)

        # validasi
        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')
    
    def test_d_failed_register_with_all_blank_fill(self):
        # steps
        driver = self.browser #buka web browser

        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("") # kosongi nama
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("") # kosongi email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("") # kosongi password
        time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(1)
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click() #klik tombol OK untuk menutup popup
        time.sleep(1)

        # validasi
        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__":
    unittest.main()