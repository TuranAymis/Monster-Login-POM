import unittest
from pages.login_page import LoginPage
from utils.driver_manager import DriverManager

class SuccessfulLoginTest(unittest.TestCase):
    def setUp(self):
        # Her test senaryosu başlamadan önce çalışır
        self.driver_manager = DriverManager()
        self.driver = self.driver_manager.get_driver()
        self.login_page = LoginPage(self.driver)

    def test_successful_login(self):
        # Başarılı login testi
        self.login_page.open_page("https://www.monsternotebook.com.tr/giris")

        # Geçerli kullanıcı bilgileri
        email = "turan.aymis@monsternotebook.com"  # **Buraya geçerli bir e-posta adresi girin**
        password = "test123"  # **Buraya geçerli bir şifre girin**

        self.login_page.enter_credentials(email, password)
        self.login_page.click_giris_yap_button_form()

        # Doğrulama: Login'in başarılı olup olmadığını kontrol et
        self.assertTrue(self.login_page.is_login_successful(), "Login işlemi başarısız oldu!")

    def tearDown(self):
        # Her test senaryosu bittikten sonra çalışır
        self.driver_manager.quit_driver()

if __name__ == "__main__":
    unittest.main()