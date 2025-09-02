from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Elementlerin görünmesini beklemek için

        # Sayfa elementleri için locators
        self.email_input = (By.XPATH, "//input[@id='UserNameOrEmail']")
        self.password_input = (By.XPATH, "(//input[@id='Password'])[1]")
        self.giris_yap_button_form = (By.XPATH, "(//button[@class='btn btn-primary fs-16 fw-500 w-100'])[1]")
        self.successful_login_element = (By.XPATH, "//div[@class='main-text d-login login-username text-white']")

    def open_page(self, url):
        self.driver.get(url)

    def enter_credentials(self, email, password):
        # E-posta ve şifre alanlarına bilgileri gir
        self.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_giris_yap_button_form(self):
        # Form içindeki "Giriş Yap" butonuna tıkla
        self.driver.find_element(*self.giris_yap_button_form).click()

    def is_login_successful(self):
        # Başarılı login sonrası "Hesabım" yazısının göründüğünü doğrula
        try:
            self.wait.until(EC.visibility_of_element_located(self.successful_login_element))
            return True
        except:
            return False