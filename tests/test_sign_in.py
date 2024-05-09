from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import StellarBurgersLocators
from conftest import driver
from data import ValidData


class TestSignIn:
    def test_sign_in_from_home_page(self, driver):
        driver.find_element(*StellarBurgersLocators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_register_in_forms))
        driver.find_element(*StellarBurgersLocators.input_email).send_keys(ValidData.email)
        driver.find_element(*StellarBurgersLocators.input_password).send_keys(ValidData.password)
        driver.find_element(*StellarBurgersLocators.button_login).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_make_the_order))
        assert driver.find_element(*StellarBurgersLocators.button_make_the_order).is_displayed()

    def test_sign_in_from_home_page_header(self, driver):
        driver.find_element(*StellarBurgersLocators.button_personal_account).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_register_in_forms))
        driver.find_element(*StellarBurgersLocators.input_email).send_keys(ValidData.email)
        driver.find_element(*StellarBurgersLocators.input_password).send_keys(ValidData.password)
        driver.find_element(*StellarBurgersLocators.button_login).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_personal_account))
        assert driver.find_element(*StellarBurgersLocators.button_personal_account).is_displayed()

    def test_sign_in_from_registration_form(self, driver):
        driver.find_element(*StellarBurgersLocators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_register_in_forms))
        driver.find_element(*StellarBurgersLocators.button_register_in_forms).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_submit))
        driver.find_element(*StellarBurgersLocators.button_login_in_forms).click()
        driver.find_element(*StellarBurgersLocators.input_email).send_keys(ValidData.email)
        driver.find_element(*StellarBurgersLocators.input_password).send_keys(ValidData.password)
        driver.find_element(*StellarBurgersLocators.button_login).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_personal_account))
        assert driver.find_element(*StellarBurgersLocators.button_personal_account).is_displayed()

    def test_sign_in_from_forgot_password_form(self, driver):
        driver.find_element(*StellarBurgersLocators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_forgot_password))
        driver.find_element(*StellarBurgersLocators.button_forgot_password).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_login_in_forms))
        driver.find_element(*StellarBurgersLocators.button_login_in_forms).click()
        driver.find_element(*StellarBurgersLocators.input_email).send_keys(ValidData.email)
        driver.find_element(*StellarBurgersLocators.input_password).send_keys(ValidData.password)
        driver.find_element(*StellarBurgersLocators.button_login).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_personal_account))
        assert driver.find_element(*StellarBurgersLocators.button_personal_account).is_displayed()
