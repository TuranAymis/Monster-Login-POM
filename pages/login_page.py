from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Elementlerin görünmesini beklemek için

        # Sayfa elementleri için locators
        self.giris_yap_button_top = (By.XPATH, "//div[@class='header-right']//a[@title='Giriş Yap']")
        self.email_input = (By.ID, "user-email")
        self.password_input = (By.ID, "user-password")
        self.giris_yap_button_form = (By.XPATH, "//button[@type='submit'][normalize-space()='Giriş Yap']")
        self.successful_login_element = (By.XPATH, "//div[@class='header-top-menu']//a[contains(text(), 'Hesabım')]")

    def open_page(self, url):
        self.driver.get(url)

    def click_giris_yap_button_top(self):
        # Ana sayfadaki "Giriş Yap" butonuna tıkla
        self.wait.until(EC.element_to_be_clickable(self.giris_yap_button_top)).click()

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