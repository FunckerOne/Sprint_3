from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import StellarBurgersLocators
from conftest import driver
from data import ValidData


class TestNavigateToConstructor:
    def test_navig_from_account_to_construct_header(self, driver):
        driver.find_element(*StellarBurgersLocators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_register_in_forms))
        driver.find_element(*StellarBurgersLocators.input_email).send_keys(ValidData.email)
        driver.find_element(*StellarBurgersLocators.input_password).send_keys(ValidData.password)
        driver.find_element(*StellarBurgersLocators.button_login).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_personal_account))
        driver.find_element(*StellarBurgersLocators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.profile))
        driver.find_element(*StellarBurgersLocators.header_of_page_constructor).click()
        assert driver.find_element(*StellarBurgersLocators.button_make_the_order).is_displayed()

    def test_navig_from_account_to_logo(self, driver):
        driver.find_element(*StellarBurgersLocators.button_personal_account).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_register_in_forms))
        driver.find_element(*StellarBurgersLocators.input_email).send_keys(ValidData.email)
        driver.find_element(*StellarBurgersLocators.input_password).send_keys(ValidData.password)
        driver.find_element(*StellarBurgersLocators.button_login).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_personal_account))
        driver.find_element(*StellarBurgersLocators.button_personal_account).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.profile))
        driver.find_element(*StellarBurgersLocators.logo).click()
        assert driver.find_element(*StellarBurgersLocators.button_make_the_order).is_displayed()
