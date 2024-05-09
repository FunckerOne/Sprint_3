from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import StellarBurgersLocators
from conftest import driver
from data import ValidData


class TestLogout:
    def test_logout_from_account(self, driver):
        driver.find_element(*StellarBurgersLocators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_register_in_forms))
        driver.find_element(*StellarBurgersLocators.input_email).send_keys(ValidData.email)
        driver.find_element(*StellarBurgersLocators.input_password).send_keys(ValidData.password)
        driver.find_element(*StellarBurgersLocators.button_login).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_personal_account))
        driver.find_element(*StellarBurgersLocators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.profile))
        driver.find_element(*StellarBurgersLocators.button_logout).click()
        WebDriverWait(driver, 5).until((expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_login)))
        assert driver.find_element(*StellarBurgersLocators.button_login).is_displayed()
