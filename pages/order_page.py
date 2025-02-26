import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    locators = OrderPageLocators

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://qa-scooter.praktikum-services.ru/order"

    @allure.step("Открыть страницу заказа")
    def open_order_url(self):
        self.driver.get(self.url)

    @allure.step("Установить имя: {name}")
    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.name_input).send_keys(name)

    @allure.step("Установить фамилию: {last_name}")
    def set_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.last_name_input).send_keys(last_name)

    @allure.step("Установить адрес: {address}")
    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.address_input).send_keys(address)

    @allure.step("Выбрать станцию метро: {subway}")
    def set_subway(self, subway):
        wait = WebDriverWait(self.driver, 10)
        input_field = wait.until(EC.element_to_be_clickable(OrderPageLocators.subway_input))
        input_field.click()
        input_field.send_keys(subway)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".select-search__row"))).click()

    @allure.step("Установить номер телефона: {telephone_number}")
    def set_telephone_number(self, telephone_number):
        self.driver.find_element(*OrderPageLocators.telephone_number_input).send_keys(telephone_number)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()

    @allure.step("Установить дату: {date}")
    def set_date(self, date):
        day = date.split('.')[0]
        self.driver.find_element(*OrderPageLocators.date_input).send_keys(date)
        self.select_specific_date(day)

    @allure.step("Выбрать конкретную дату: {day}")
    def select_specific_date(self, day):
        date_picker_day = self.driver.find_element(By.XPATH,
                                                   f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']")
        date_picker_day.click()

    @allure.step("Установить срок аренды: {rental_period}")
    def set_rental_period(self, rental_period):
        self.driver.find_element(*OrderPageLocators.rental_period_input).click()
        options = self.driver.find_elements(By.CSS_SELECTOR, '.Dropdown-option[role="option"]')
        for option in options:
            if option.text == rental_period:
                option.click()
                break

    @allure.step("Выбрать цвет самоката: {color}")
    def click_scooter_color(self, color):
        if color.lower() == "black":
            self.driver.find_element(*OrderPageLocators.black_scooter).click()
        elif color.lower() == "grey":
            self.driver.find_element(*OrderPageLocators.grey_scooter).click()

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.order_button).click()

    @allure.step("Нажать кнопку подтверждения заказа")
    def click_verification_button(self):
        self.driver.find_element(*OrderPageLocators.verification_button).click()

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

    @allure.step("Открыть страницу по URL: {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        return self.driver.find_element(*OrderPage.locators.confirmation_message).text
