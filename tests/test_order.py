import allure
import pytest
from selenium import webdriver

from pages.order_page import OrderPage


class TestOrder:
    driver = None
    url = "https://qa-scooter.praktikum-services.ru/order"

    @classmethod
    def setup_method(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @classmethod
    def teardown_method(cls):
        cls.driver.quit()

    @pytest.mark.parametrize(
        'name,last_name,address,subway,telephone_number,date,rental_period,color',
        [
            ('Иван', 'Иванов', 'Москва, ул. Пушкина, д. 1', 'Аэропорт', '11111111111', '26.02.2025', 'сутки', 'black'),
            ('Сергей', 'Сергеев', 'Москва, ул. Ленина, д. 2', 'Черкизовская', '22222222222', '15.03.2025',
             'двое суток', 'grey')
        ])
    @allure.feature("Order Page")
    @allure.story("Успешное оформление заказа самоката")
    def test_order_page(self, name, last_name, address, subway, telephone_number, date, rental_period, color):
        with allure.step("Инициализация объекта страницы заказа"):
            page = OrderPage(self.driver)

        with allure.step("Открыть URL страницы заказа"):
            page.open_page(self.url)

        with allure.step("Заполнить и отправить форму заказа"):
            page.order(name, last_name, address, subway, telephone_number, date, rental_period, color)

        with allure.step("Проверить сообщение подтверждения заказа"):
            order_confirmation = self.driver.find_element(*OrderPage.confirmation_message).text
            assert "Номер заказа:" in order_confirmation and "Запишите его" in order_confirmation
