import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

class TestRegister(unittest.TestCase):
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_failed_register_with_email_registered(self):
        # steps
        driver = self.browser #buka web browser
        # wait = WebDriverWait(driver, 10)

        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        driver.find_element(By.ID, "signUp").click()
        # time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("agustin anisa") # isi nama
        # time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("agustin@gmail.com") # isi email yang sudah didaftarkan
        # time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("passwordagustin") # isi password
        # time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(1)
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text
        # element = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[@id='swal2-title']")))
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click()
        time.sleep(1)

        # validasi
        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')
    
    def test_a_failed_register_with_empty_name(self):
        # steps
        driver = self.browser #buka web browser
        # wait = WebDriverWait(driver, 10)

        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        driver.find_element(By.ID, "signUp").click()
        # time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("") # isi nama
        # time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("agustin@gmail.com") # isi email yang sudah didaftarkan
        # time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("passwordagustin") # isi password
        # time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(1)
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text
        # element = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[@id='swal2-title']")))
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click()
        time.sleep(1)

        # validasi
        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def test_b_failed_register_with_empty_email(self):
        # steps
        driver = self.browser #buka web browser
        # wait = WebDriverWait(driver, 10)

        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        driver.find_element(By.ID, "signUp").click()
        # time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("agustin anisa") # isi nama
        # time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("") # isi email yang sudah didaftarkan
        # time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("passwordagustin") # isi password
        # time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(1)
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text
        # element = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[@id='swal2-title']")))
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click()
        time.sleep(1)

        # validasi
        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def test_c_failed_register_with_empty_password(self):
        # steps
        driver = self.browser #buka web browser
        # wait = WebDriverWait(driver, 10)

        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        driver.find_element(By.ID, "signUp").click()
        # time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("agustin anisa") # isi nama
        # time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("agustin@gmail.com") # isi email yang sudah didaftarkan
        # time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("") # isi password
        # time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(1)
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text
        # element = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[@id='swal2-title']")))
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click()
        time.sleep(1)

        # validasi
        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__":
    unittest.main()