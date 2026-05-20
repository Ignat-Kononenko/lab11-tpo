import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_page_title(driver):
    driver.get("http://localhost:8000")
    assert "CI/CD Лабораторная" in driver.title

def test_valid_name(driver):
    driver.get("http://localhost:8000")
    driver.find_element(By.ID, "username").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    greeting = driver.find_element(By.ID, "greeting").text
    assert "Привет, Иван!" in greeting

def test_empty_name(driver):
    driver.get("http://localhost:8000")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    greeting = driver.find_element(By.ID, "greeting").text
    assert "Пожалуйста, введите имя" in greeting

def test_button_text(driver):
    driver.get("http://localhost:8000")
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    assert button.text == "Отправить"