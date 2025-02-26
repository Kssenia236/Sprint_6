import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators

    def open_base_url(self):
        with allure.step("Открытие базового URL"):
            self.driver.get(self.url)

    def click_order_button(self):
        with allure.step("Ожидание кликабельности кнопки заказа"):
            order_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.order_button_1)
            )
        with allure.step("Прокрутка к первой кнопке заказа и клик по ней"):
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                       order_button)
            ActionChains(self.driver).move_to_element(order_button).click().perform()
        with allure.step("Ожидание перехода на страницу заказа"):
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("https://qa-scooter.praktikum-services.ru/order")
            )

    def click_botom_order_button(self):
        with allure.step("Ожидание появления кнопки заказа внизу страницы"):
            order_button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators.order_button_2)
            )
        with allure.step("Прокрутка к кнопке заказа внизу страницы"):
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                       order_button_element)
        with allure.step("Ожидание кликабельности кнопки заказа внизу страницы"):
            order_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.order_button_2)
            )
        with allure.step("Прокрутка и клик по кнопке заказа внизу страницы"):
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)
            ActionChains(self.driver).move_to_element(order_button).click().perform()
        with allure.step("Ожидание перехода на страницу заказа"):
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("https://qa-scooter.praktikum-services.ru/order")
            )

    def click_questions_button(self, button_number, expected_text):
        with allure.step("Прокрутка страницы до нижней части"):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        wait = WebDriverWait(self.driver, 5)
        button_locator = getattr(MainPage.locators, f'title_button_{button_number}')

        with allure.step(f"Ожидание появления кнопки вопроса {button_number}"):
            target = wait.until(EC.presence_of_element_located(button_locator))

        with allure.step(f"Прокрутка кнопки вопроса {button_number} в видимую область"):
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)

        with allure.step(f"Ожидание кликабельности кнопки вопроса {button_number} и выполнение клика"):
            wait.until(EC.element_to_be_clickable(button_locator))
            self.driver.execute_script("arguments[0].click();", target)

        with allure.step("Ожидание отображения ответа на вопрос"):
            element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[text()='{expected_text}']")))
