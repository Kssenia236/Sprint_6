import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class TestQuestions():

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_click_question_1(self):
        with allure.step("Тест вопроса 1"):
            page = BasePage(self.driver)
            page.open_base_url()
            with allure.step("Прокрутка до нижней части страницы"):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait = WebDriverWait(self.driver, 5)
            with allure.step("Ожидание, пока кнопка вопроса 1 станет кликабельной"):
                wait.until(EC.element_to_be_clickable(page.title_button_1))
            with allure.step("Клик по кнопке вопроса 1"):
                page.click_title_button_1()
            with allure.step("Ожидание видимости ответа"):
                element = wait.until(EC.visibility_of_element_located(
                    (By.XPATH, "//*[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")))
            with allure.step("Проверка отображения ответа"):
                assert element.is_displayed()

    def test_click_question_2(self):
        with allure.step("Тест вопроса 2"):
            page = BasePage(self.driver)
            page.open_base_url()
            with allure.step("Прокрутка до нижней части страницы"):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait = WebDriverWait(self.driver, 5)
            with allure.step("Ожидание появления кнопки вопроса 2"):
                wait.until(EC.presence_of_element_located(page.title_button_2))
            with allure.step("Прокрутка кнопки вопроса 2 в видимую область"):
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",
                                           self.driver.find_element(*page.title_button_2))
            with allure.step("Ожидание кликабельности кнопки вопроса 2 и нажатие"):
                wait.until(EC.element_to_be_clickable(page.title_button_2))
                self.driver.execute_script("arguments[0].click();",
                                           self.driver.find_element(*page.title_button_2))
            with allure.step("Ожидание видимости ответа"):
                element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                       "//*[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")))
            with allure.step("Проверка отображения ответа"):
                assert element.is_displayed()

    def test_click_question_3(self):
        with allure.step("Тест вопроса 3"):
            page = BasePage(self.driver)
            page.open_base_url()
            with allure.step("Прокрутка до нижней части страницы"):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait = WebDriverWait(self.driver, 5)
            with allure.step("Ожидание появления кнопки вопроса 3"):
                target = wait.until(EC.presence_of_element_located(page.title_button_3))
            with allure.step("Прокрутка кнопки вопроса 3 в видимую область"):
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)
            with allure.step("Ожидание кликабельности кнопки вопроса 3 и нажатие"):
                wait.until(EC.element_to_be_clickable(page.title_button_3))
                self.driver.execute_script("arguments[0].click();", target)
            with allure.step("Ожидание видимости ответа"):
                element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                       "//*[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")))
            with allure.step("Проверка отображения ответа"):
                assert element.is_displayed()

    def test_click_question_4(self):
        with allure.step("Тест вопроса 4"):
            page = BasePage(self.driver)
            page.open_base_url()
            with allure.step("Прокрутка до нижней части страницы"):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait = WebDriverWait(self.driver, 5)
            with allure.step("Ожидание появления кнопки вопроса 4"):
                target = wait.until(EC.presence_of_element_located(page.title_button_4))
            with allure.step("Прокрутка кнопки вопроса 4 в видимую область"):
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)
            with allure.step("Ожидание кликабельности кнопки вопроса 4 и нажатие"):
                wait.until(EC.element_to_be_clickable(page.title_button_4))
                self.driver.execute_script("arguments[0].click();", target)
            with allure.step("Ожидание видимости ответа"):
                element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                       "//*[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")))
            with allure.step("Проверка отображения ответа"):
                assert element.is_displayed()

    def test_click_question_5(self):
        with allure.step("Тест вопроса 5"):
            page = BasePage(self.driver)
            page.open_base_url()
            with allure.step("Прокрутка до нижней части страницы"):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait = WebDriverWait(self.driver, 5)
            with allure.step("Ожидание появления кнопки вопроса 5"):
                target = wait.until(EC.presence_of_element_located(page.title_button_5))
            with allure.step("Прокрутка кнопки вопроса 5 в видимую область"):
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)
            with allure.step("Ожидание кликабельности кнопки вопроса 5 и нажатие"):
                wait.until(EC.element_to_be_clickable(page.title_button_5))
                self.driver.execute_script("arguments[0].click();", target)
            with allure.step("Ожидание видимости ответа"):
                element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                       "//*[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")))
            with allure.step("Проверка отображения ответа"):
                assert element.is_displayed()

    def test_click_question_6(self):
        with allure.step("Тест вопроса 6"):
            page = BasePage(self.driver)
            page.open_base_url()
            with allure.step("Прокрутка до нижней части страницы"):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait = WebDriverWait(self.driver, 5)
            with allure.step("Ожидание появления кнопки вопроса 6"):
                target = wait.until(EC.presence_of_element_located(page.title_button_6))
            with allure.step("Прокрутка кнопки вопроса 6 в видимую область"):
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)
            with allure.step("Ожидание кликабельности кнопки вопроса 6 и нажатие"):
                wait.until(EC.element_to_be_clickable(page.title_button_6))
                self.driver.execute_script("arguments[0].click();", target)
            with allure.step("Ожидание видимости ответа"):
                element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                       "//*[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']")))
            with allure.step("Проверка отображения ответа"):
                assert element.is_displayed()

    def test_click_question_7(self):
        with allure.step("Тест вопроса 7"):
            page = BasePage(self.driver)
            page.open_base_url()
            with allure.step("Прокрутка до нижней части страницы"):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait = WebDriverWait(self.driver, 5)
            with allure.step("Ожидание появления кнопки вопроса 7"):
                target = wait.until(EC.presence_of_element_located(page.title_button_7))
            with allure.step("Прокрутка кнопки вопроса 7 в видимую область"):
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)
            with allure.step("Ожидание кликабельности кнопки вопроса 7 и нажатие"):
                wait.until(EC.element_to_be_clickable(page.title_button_7))
                self.driver.execute_script("arguments[0].click();", target)
            with allure.step("Ожидание видимости ответа"):
                element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                       "//*[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")))
            with allure.step("Проверка отображения ответа"):
                assert element.is_displayed()

    def test_click_question_8(self):
        with allure.step("Тест вопроса 8"):
            page = BasePage(self.driver)
            page.open_base_url()
            with allure.step("Прокрутка до нижней части страницы"):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait = WebDriverWait(self.driver, 5)
            with allure.step("Ожидание появления кнопки вопроса 8"):
                target = wait.until(EC.presence_of_element_located(page.title_button_8))
            with allure.step("Прокрутка кнопки вопроса 8 в видимую область"):
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)
            with allure.step("Ожидание кликабельности кнопки вопроса 8 и нажатие"):
                wait.until(EC.element_to_be_clickable(page.title_button_8))
                self.driver.execute_script("arguments[0].click();", target)
            with allure.step("Ожидание видимости ответа"):
                element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                       "//*[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']")))
            with allure.step("Проверка отображения ответа"):
                assert element.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
