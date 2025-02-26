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


    @pytest.mark.parametrize(
        'name,last_name,address,subway,telephone_number,date,rental_period,color',
        [
            ('Иван', 'Иванов', 'Москва, ул. Пушкина, д. 1', 'Аэропорт', '11111111111', '26.02.2025', 'сутки', 'black'),
            ('Сергей', 'Сергеев', 'Москва, ул. Ленина, д. 2', 'Черкизовская', '22222222222', '15.03.2025',
             'двое суток', 'grey')
        ])
    def test_order_page(self, name, last_name, address, subway, telephone_number, date, rental_period, color):
        page = OrderPage(self.driver)
        page.open_page(self.url)
        page.order(name, last_name, address, subway, telephone_number, date, rental_period, color)
        order_confirmation = page.confirm_order()
        assert "Номер заказа:" in order_confirmation and "Запишите его" in order_confirmation


    @classmethod
    def teardown_method(cls):
        cls.driver.quit()
