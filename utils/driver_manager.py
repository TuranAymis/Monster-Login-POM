from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class DriverManager:
    def __init__(self):
        self.driver = None

    def get_driver(self):
        # WebDriverManager kullanarak Chrome sürücüsünü otomatik olarak indir ve başlat
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()