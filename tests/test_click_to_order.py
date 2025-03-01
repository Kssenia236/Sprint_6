
from selenium import webdriver
from pages.main_page import MainPage

class TestClickOrder:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_click_order_button_1(self):
        page = MainPage(self.driver)
        page.open_base_url()
        page.click_order_button()
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/order"
        page.open_base_url()

    def test_click_order_button_2(self):
        page = MainPage(self.driver)
        page.open_base_url()
        page.click_botom_order_button()
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()