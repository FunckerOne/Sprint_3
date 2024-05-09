from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import StellarBurgersLocators
from conftest import driver
from helpers import create_random_email
from data import ValidData


class TestSignUpRegistration:
    def test_sign_up_positiv(self, driver):
        random_email = create_random_email()
        driver.find_element(*StellarBurgersLocators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_register_in_forms))
        driver.find_element(*StellarBurgersLocators.button_register_in_forms).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_submit))
        driver.find_element(*StellarBurgersLocators.input_name).send_keys(ValidData.username)
        driver.find_element(*StellarBurgersLocators.input_email).send_keys(random_email)
        driver.find_element(*StellarBurgersLocators.input_password).send_keys(ValidData.password)
        driver.find_element(*StellarBurgersLocators.button_submit).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_login))
        assert driver.find_element(*StellarBurgersLocators.button_register_in_forms).is_displayed()

    def test_sign_up_notification_incorrect_password(self, driver):
        driver.find_element(*StellarBurgersLocators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_register_in_forms))
        driver.find_element(*StellarBurgersLocators.button_register_in_forms).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_submit))
        driver.find_element(*StellarBurgersLocators.input_name).send_keys(ValidData.username)
        driver.find_element(*StellarBurgersLocators.input_email).send_keys(ValidData.email)
        driver.find_element(*StellarBurgersLocators.input_password).send_keys("12345")
        driver.find_element(*StellarBurgersLocators.button_submit).click()
        assert driver.find_element(*StellarBurgersLocators.notification_incorrect_password).text == 'Некорректный пароль'
