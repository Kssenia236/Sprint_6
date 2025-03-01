from selenium.webdriver.common.by import By


class MainPageLocators:
    order_button_1 = (By.XPATH, '//*[@id="root"]//div[2]/button[1]')
    order_button_2 = (By.XPATH, '//*[@id="root"]//div[5]/button')
    title_button_1 = (By.XPATH, '//*[@id="accordion__heading-0"]')
    title_button_2 = (By.XPATH, '//*[@id="accordion__heading-1"]')
    title_button_3 = (By.XPATH, '//*[@id="accordion__heading-2"]')
    title_button_4 = (By.XPATH, '//*[@id="accordion__heading-3"]')
    title_button_5 = (By.XPATH, '//*[@id="accordion__heading-4"]')
    title_button_6 = (By.XPATH, '//*[@id="accordion__heading-5"]')
    title_button_7 = (By.XPATH, '//*[@id="accordion__heading-6"]')
    title_button_8 = (By.XPATH, '//*[@id="accordion__heading-7"]')

class OrderPageLocators:
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