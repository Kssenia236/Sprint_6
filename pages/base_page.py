from selenium import webdriver

class BasePage:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.url = "https://qa-scooter.praktikum-services.ru"


