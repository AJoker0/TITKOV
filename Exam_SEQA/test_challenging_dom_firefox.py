import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    service = FirefoxService(
        executable_path=r"C:\Users\andri\Desktop\VUM\firstscript\SEQA\geckodriver.exe"
    )
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_challenging_dom_page(driver):
    driver.get("https://the-internet.herokuapp.com/challenging_dom")

    WebDriverWait(driver, 10).until(EC.title_contains("The Internet"))
    assert "The Internet" in driver.title

    heading = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#content > div > h3"))
    )
    assert heading.text == "Challenging DOM"

    driver.save_screenshot("01_page_loaded.png")

    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )
    assert table.is_displayed(), "Таблица не отображается"

    blue = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "button"))
    )
    green = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "button.success"))
    )
    red = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "button.alert"))
    )
    assert blue.is_displayed() and green.is_displayed() and red.is_displayed()

    driver.save_screenshot("02_buttons_checked.png")

    headers = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table th"))
    )
    expected = ["Lorem", "Ipsum", "Dolor", "Sit", "Amet", "Diceret", "Action"]
    actual = [h.text for h in headers]
    assert actual == expected, f"Неверные заголовки таблицы: {actual}"

    canvas = driver.find_element(By.ID, "canvas")
    assert canvas.is_displayed()
    canvas.screenshot("03_canvas_only.png")

    driver.save_screenshot("04_final.png")

    time.sleep(5)
