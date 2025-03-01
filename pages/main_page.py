import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators

    def __init__(self, driver):
        super().__init__(driver, url="https://qa-scooter.praktikum-services.ru")

    @allure.step("Открытие главной страницы")
    def open_base_url(self):
        self.open_page()

    @allure.step("Клик по верхней кнопке заказа")
    def click_order_button(self):
        button = self.find_clickable_element(self.locators.order_button_1)
        self.scroll_to_element(button)
        self.click_element(button)
        self.wait_for_url_contains("order")

    @allure.step("Клик по нижней кнопке заказа")
    def click_botom_order_button(self):
        self.scroll_to_bottom()
        button = self.wait_and_click_element(self.locators.order_button_2)
        self.wait_for_url_contains("order")

    @allure.step("Клик по кнопке вопроса {button_number}")
    def click_questions_button(self, button_number, expected_text):
        self.scroll_to_bottom()
        time.sleep(1)
        question_locator = (By.ID, f"accordion__heading-{button_number - 1}")
        question = self.wait_and_click_element(question_locator, timeout=10)
        panel_locator = (By.ID, f"accordion__panel-{button_number - 1}")
        answer_panel = self.find_element(panel_locator)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(panel_locator)
        )
