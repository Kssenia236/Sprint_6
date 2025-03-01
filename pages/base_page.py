from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def scroll_to_element(self, element, center=True):
        if center:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                element
            )
        else:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_element(self, element):
        ActionChains(self.driver).move_to_element(element).click().perform()

    def wait_for_url_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_part)
        )

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def open_page(self, url=None):
        self.driver.get(url or self.url)

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def select_from_dropdown(self, dropdown_locator, option_text, option_css='.Dropdown-option[role="option"]'):
        self.click(dropdown_locator)
        options = self.find_elements((By.CSS_SELECTOR, option_css))
        for option in options:
            if option.text == option_text:
                option.click()
                break

    def wait_and_click_element(self, locator, timeout=10):
        element = self.find_clickable_element(locator, timeout)
        element.click()
        return element

    def wait_for_element_and_send_keys(self, locator, text, timeout=10):
        element = self.find_clickable_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        return element
