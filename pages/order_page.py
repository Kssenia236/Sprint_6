import allure
from selenium.webdriver.common.by import By
from locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    locators = OrderPageLocators

    def __init__(self, driver):
        super().__init__(driver, url="https://qa-scooter.praktikum-services.ru/order")

    @allure.step("Открыть страницу заказа")
    def open_order_url(self):
        self.open_page()

    @allure.step("Установить имя: {name}")
    def set_name(self, name):
        self.input_text(self.locators.name_input, name)

    @allure.step("Установить фамилию: {last_name}")
    def set_last_name(self, last_name):
        self.input_text(self.locators.last_name_input, last_name)

    @allure.step("Установить адрес: {address}")
    def set_address(self, address):
        self.input_text(self.locators.address_input, address)

    @allure.step("Выбрать станцию метро: {subway}")
    def set_subway(self, subway):
        input_field = self.wait_and_click_element(self.locators.subway_input)
        input_field.send_keys(subway)
        self.click((By.CSS_SELECTOR, ".select-search__row"))

    @allure.step("Установить номер телефона: {telephone_number}")
    def set_telephone_number(self, telephone_number):
        self.input_text(self.locators.telephone_number_input, telephone_number)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click(self.locators.next_button)

    @allure.step("Установить дату: {date}")
    def set_date(self, date):
        day = date.split('.')[0]
        self.input_text(self.locators.date_input, date)
        self.select_specific_date(day)

    @allure.step("Выбрать конкретную дату: {day}")
    def select_specific_date(self, day):
        self.click((By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']"))

    @allure.step("Установить срок аренды: {rental_period}")
    def set_rental_period(self, rental_period):
        self.select_from_dropdown(self.locators.rental_period_input, rental_period)

    @allure.step("Выбрать цвет самоката: {color}")
    def click_scooter_color(self, color):
        if color.lower() == "black":
            self.click(self.locators.black_scooter)
        elif color.lower() == "grey":
            self.click(self.locators.grey_scooter)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        self.click(self.locators.order_button)

    @allure.step("Нажать кнопку подтверждения заказа")
    def click_verification_button(self):
        self.click(self.locators.verification_button)

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        return self.get_text(self.locators.confirmation_message)

    @allure.step(
        "Оформить заказ: {name}, {last_name}, {address}, {subway}, {telephone_number}, {date}, {rental_period}, {color}")
    def order(self, name, last_name, address, subway, telephone_number, date, rental_period, color):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_subway(subway)
        self.set_telephone_number(telephone_number)
        self.click_next_button()
        self.set_date(date)
        self.set_rental_period(rental_period)
        self.click_scooter_color(color)
        self.click_order_button()
        self.click_verification_button()