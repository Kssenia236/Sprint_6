import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class TestClickOrder():

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.story("Тест нажатия на первую кнопку заказа")
    def test_click_order_button_1(self):
        with allure.step("Открыть страницу и инициализировать BasePage"):
            page = BasePage(self.driver)
            page.open_base_url()
        with allure.step("Дождаться, пока кнопка 'Заказать 1' станет кликабельной"):
            order_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((BasePage.order_button_1[0], BasePage.order_button_1[1]))
            )
        with allure.step("Прокрутить до кнопки 'Заказать 1' и нажать"):
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                       order_button)
            ActionChains(self.driver).move_to_element(order_button).click().perform()
        with allure.step("Дождаться, пока страница перейдёт в раздел оформления заказа"):
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be("https://qa-scooter.praktikum-services.ru/order")
            )
        with allure.step("Проверить, что текущий URL соответствует странице оформления заказа"):
            assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/order"
        with allure.step("Вернуться на базовый URL"):
            page.open_base_url()

    @allure.story("Тест нажатия на вторую кнопку заказа")
    def test_click_order_button_2(self):
        with allure.step("Открыть страницу и инициализировать BasePage"):
            page = BasePage(self.driver)
            page.open_base_url()
        with allure.step("Дождаться появления кнопки 'Заказать 2'"):
            order_button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((BasePage.order_button_2[0], BasePage.order_button_2[1]))
            )
        with allure.step("Прокрутить до кнопки 'Заказать 2'"):
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                       order_button_element)
        with allure.step("Дождаться, пока кнопка 'Заказать 2' станет кликабельной, и нажать"):
            order_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((BasePage.order_button_2[0], BasePage.order_button_2[1]))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)
            ActionChains(self.driver).move_to_element(order_button).click().perform()
        with allure.step("Дождаться, пока страница перейдёт в раздел оформления заказа"):
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be("https://qa-scooter.praktikum-services.ru/order")
            )
        with allure.step("Проверить, что текущий URL соответствует странице оформления заказа"):
            assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()
