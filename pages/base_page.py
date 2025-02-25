from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage:

    order_button_1 = [By.XPATH, '//*[@id="root"]//div[2]/button[1]']
    order_button_2 = [By.XPATH, '//*[@id="root"]//div[5]/button']
    title_button_1 = [By.XPATH, '//*[@id="accordion__heading-0"]']
    title_button_2 = [By.XPATH, '//*[@id="accordion__heading-1"]']
    title_button_3 = [By.XPATH, '//*[@id="accordion__heading-2"]']
    title_button_4 = [By.XPATH, '//*[@id="accordion__heading-3"]']
    title_button_5 = [By.XPATH, '//*[@id="accordion__heading-4"]']
    title_button_6 = [By.XPATH, '//*[@id="accordion__heading-5"]']
    title_button_7 = [By.XPATH, '//*[@id="accordion__heading-6"]']
    title_button_8 = [By.XPATH, '//*[@id="accordion__heading-7"]']


    def __init__(self, driver: webdriver):
        self.driver = driver
        self.url = "https://qa-scooter.praktikum-services.ru"

    def open_base_url(self):
        self.driver.get(self.url)

    def click_order_button(self):
        self.driver.find_element(*self.order_button_1).click()

    def click_title_button_1(self):
        self.driver.find_element(*self.title_button_1).click()


    def open_page(self, url):
        self.driver.get(url)
