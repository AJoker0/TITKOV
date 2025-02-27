import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

GECKODRIVER_PATH = r"C:\Users\andri\Desktop\первый урок джавы\SEQA\geckodriver.exe"

# 🔹 Данные для аутентификации
CRED = dict(admin="admin", wrong42="A22")

class TestBasicAuth(unittest.TestCase):

    def setUp(self):
        """ Настройка WebDriver перед тестами (Firefox) """
        self.driver = webdriver.Firefox()

    def test_basic_auth_correct_credentials(self):
        """ ✅ Тест с правильными данными (должен пройти) """
        self.url = f"https://{CRED['admin']}:{CRED['admin']}@the-internet.herokuapp.com/basic_auth"
        self.driver.get(self.url)
        driver = self.driver

        # Проверяем заголовок страницы
        self.assertIn("The Internet", driver.title)

        # Проверяем контент страницы
        content = driver.find_element(By.ID, "content")
        self.assertIn("Congratulations", content.text)  # ✅ Должен быть успешный вход

        # Делаем скриншот
        driver.save_screenshot("downloads_success.png")

    def test_basic_auth_incorrect_credentials(self):
        """ ❌ Тест с НЕПРАВИЛЬНЫМИ данными (должен НЕ авторизоваться) """
        self.url = f"https://wrong42:{CRED['wrong42']}@the-internet.herokuapp.com/basic_auth"
        self.driver.get(self.url)
        driver = self.driver

        #🔹 Проверяем, появилось ли всплывающее окно (Alert)
        try:
            alert = Alert(driver)
            print("⚠️ Обнаружен диалог авторизации! Закрываем...")
            alert.dismiss()
        except NoAlertPresentException:
            print("✅ Диалог авторизации не появился (что странно 🤔)")
            raise

        # 🔹 Проверяем, что контент НЕ содержит "Congratulations"
        print('self.driver.title', self.driver.title)
        self.assertNotIn("The Internet", self.driver.title)  # Должен провалиться
        driver.save_screenshot("downloads_incorrect.png")

    def test_basic_auth_without_credentials(self):
        """ ❌ Тест БЕЗ логина и пароля (должен НЕ авторизоваться) """
        self.url = "https://the-internet.herokuapp.com/basic_auth"
        self.driver.get(self.url)
        driver = self.driver

        # 🔹 Проверяем, появилось ли всплывающее окно (Alert)
        try:
            alert = Alert(driver)
            print("⚠️ Обнаружен диалог авторизации! Закрываем...")
            self.assertTrue(alert)
            alert.dismiss()
        except NoAlertPresentException:
            print("✅ Диалог авторизации не появился (что странно)")
            raise        

        print('self.driver.title', self.driver.title)
        self.assertNotIn("The Internet", self.driver.title)  # Должен провалиться
        driver.save_screenshot("downloads_no_credentials.png")

    def tearDown(self):
        """ Завершаем работу WebDriver """
        try:
            if self.driver:
                self.driver.quit()
        except:
            print("Ошибка при закрытии WebDriver")


if __name__ == '__main__':
    unittest.main(verbosity=2)
