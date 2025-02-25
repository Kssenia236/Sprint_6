from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrderPage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.url = "https://qa-scooter.praktikum-services.ru/order"

    name_input = (By.CSS_SELECTOR, '[placeholder="* Имя"]')
    last_name_input = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')
    address_input = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')
    subway_input = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    telephone_number_input = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')
    next_button = (By.XPATH, '//div[2]/div[3]/button')
    date_input = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')
    rental_period_input = (By.CSS_SELECTOR, '[aria-haspopup="listbox"]')
    black_scooter = (By.CSS_SELECTOR, '[for="black"]')
    grey_scooter = (By.CSS_SELECTOR, '[for="grey"]')
    comment_input = (By.CSS_SELECTOR, '[placeholder="Комментарий для курьера"]')
    order_button = (By.XPATH, '//div[3]/button[2]')
    verification_button = (By.CSS_SELECTOR, 'div.Order_Buttons__1xGrp:nth-child(2) > button:nth-child(2)')
    confirmation_message = By.CSS_SELECTOR, ".Order_Text__2broi"

    def open_order_url(self):
        self.driver.get(self.url)

    def set_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    def set_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def set_address(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)

    def set_subway(self, subway):
        wait = WebDriverWait(self.driver, 10)
        input_field = wait.until(EC.element_to_be_clickable(self.subway_input))
        input_field.click()
        input_field.send_keys(subway)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".select-search__row"))).click()

    def set_telephone_number(self, telephone_number):
        self.driver.find_element(*self.telephone_number_input).send_keys(telephone_number)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def set_date(self, date):
        day = date.split('.')[0]
        self.driver.find_element(*self.date_input).send_keys(date)
        self.select_specific_date(day)

    def select_specific_date(self, day):
        date_picker_day = self.driver.find_element(By.XPATH,
                                                   f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']")
        date_picker_day.click()

    def set_rental_period(self, rental_period):
        self.driver.find_element(*self.rental_period_input).click()
        options = self.driver.find_elements(By.CSS_SELECTOR, '.Dropdown-option[role="option"]')
        for option in options:
            if option.text == rental_period:
                option.click()
                break

    def click_scooter_color(self, color):
        if color.lower() == "black":
            self.driver.find_element(*self.black_scooter).click()
        elif color.lower() == "grey":
            self.driver.find_element(*self.grey_scooter).click()

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def click_verification_button(self):
        self.driver.find_element(*self.verification_button).click()

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

    def open_page(self, url):
        self.driver.get(url)
