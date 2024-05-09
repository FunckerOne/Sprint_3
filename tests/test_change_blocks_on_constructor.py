from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import StellarBurgersLocators
from conftest import driver


class TestChangeBlocksOnConstructor:
    def test_change_blocks_from_buns_to_sauces(self, driver):
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_login_in_main))
        driver.find_element(*StellarBurgersLocators.sauces_block).click()
        assert driver.find_element(*StellarBurgersLocators.selected_button).text == 'Соусы'

    def test_change_blocks_from_buns_to_fillings(self, driver):
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_login_in_main))
        driver.find_element(*StellarBurgersLocators.fillings_block).click()
        assert driver.find_element(*StellarBurgersLocators.selected_button).text == 'Начинки'

    def test_change_blocks_from_sauces_to_buns(self, driver):
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_login_in_main))
        driver.find_element(*StellarBurgersLocators.sauces_block).click()
        driver.find_element(*StellarBurgersLocators.buns_block).click()
        assert driver.find_element(*StellarBurgersLocators.selected_button).text == 'Булки'

    def test_change_blocks_from_sauces_to_fillings(self, driver):
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_login_in_main))
        driver.find_element(*StellarBurgersLocators.sauces_block).click()
        driver.find_element(*StellarBurgersLocators.fillings_block).click()
        assert driver.find_element(*StellarBurgersLocators.selected_button).text == 'Начинки'

    def test_change_blocks_from_fillings_to_buns(self, driver):
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_login_in_main))
        driver.find_element(*StellarBurgersLocators.fillings_block).click()
        driver.find_element(*StellarBurgersLocators.buns_block).click()
        assert driver.find_element(*StellarBurgersLocators.selected_button).text == 'Булки'

    def test_change_blocks_from_fillings_to_sauces(self, driver):
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.button_login_in_main))
        driver.find_element(*StellarBurgersLocators.fillings_block).click()
        driver.find_element(*StellarBurgersLocators.sauces_block).click()
        assert driver.find_element(*StellarBurgersLocators.selected_button).text == 'Соусы'
