from selenium.webdriver.common.by import By


class StellarBurgersLocators:

    input_name = By.XPATH, '//label[text()="Имя"]/following-sibling::input' # Поле "Имя"

    input_email = By.XPATH, './/label[text()="Email"]/following-sibling::input' # Поле Email

    input_password = By.XPATH, './/input[@name="Пароль"]' # Поле "Пароль"

    button_submit = By.XPATH, '//button[text() = "Зарегистрироваться"]' # Кнопка "Зарегистрироваться"

    notification_incorrect_password = By.XPATH, '//p[text() = "Некорректный пароль"]' # Сообщение об ошибке: пароль не прошел валидацию

    button_login_in_forms = By.XPATH, '//a[text() = "Войти"]' # Кнопка "Войти" на форме регистрации

    button_login = By.XPATH, '//button[text()="Войти"]' # Кнопка "Войти"

    button_make_the_order = By.XPATH, '//button[text()="Оформить заказ"]' # Кнопка "Оформить заказ"

    button_register_in_forms = By.XPATH, '//a[text() = "Зарегистрироваться"]' # Кнопка "Зарегистрироваться"

    button_forgot_password = By.XPATH, '//a[text() = "Восстановить пароль"]' # Кнопка "Восстановить пароль"

    profile = By.XPATH, '//a[@href = "/account/profile"]' # Раздел "Профиль"

    button_logout = By.XPATH, '//button[@type = "button"]' # Кнопка "Выйти"

    button_login_in_main = By.XPATH, './/button[text() = "Войти в аккаунт"]' # Кнопка "Войти в аккаунт" на главной

    button_personal_account = By.XPATH, '//p[text() = "Личный Кабинет"]' # Кнопка "Личный кабинет"

    header_of_page_constructor = By.XPATH, '//p[text() = "Конструктор"]' # Кнопка "Конструктор" в шапке сайта

    logo = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]' # Кликабельный логотип в шапке сайта

    selected_button = By.XPATH, ('//div[@class = '
                                 '"tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]') # Селектор

    buns_block = By.XPATH, '//span[text() = "Булки"]' # Заголовок раздела "Булки" в меню конструктора

    sauces_block = By.XPATH, '//span[text() = "Соусы"]' # Заголовок раздела "Соусы" в меню конструктора

    fillings_block = By.XPATH, '//span[text() = "Начинки"]' # Заголовок раздела "Начинки" в меню конструктора
