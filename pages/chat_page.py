from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ChatPage:
    # Locators (update these as per your actual HTML)
    CHAT_INPUT = (By.NAME, "message")  # Example selector
    
    SEND_BUTTON = (By.XPATH, "//button[@type='submit']")


    SELECT_MODEL_BUTTON = (By.XPATH, "//button[@role='combobox' and normalize-space()='Select model']")

    MESSAGES = (By.CSS_SELECTOR, ".chat-message")  # Example selector
    MODEL_OPTION = (By.XPATH, "//button[normalize-space()='gemma3:1b']")
    US_ICON = (By.XPATH,"//span[text()='US']")


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_message(self, message: str):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CHAT_INPUT)
        )
        input_box = self.driver.find_element(*self.CHAT_INPUT)
        input_box.clear()
        input_box.send_keys(message)

    def send_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEND_BUTTON)
        )
        self.driver.find_element(*self.SEND_BUTTON).click()
        


    def click_select_model(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SELECT_MODEL_BUTTON)
        )
        self.driver.find_element(*self.SELECT_MODEL_BUTTON).click()

    def choose_model_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MODEL_OPTION)
        )
        self.driver.find_element(*self.MODEL_OPTION).click()



    def get_last_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MESSAGES)
        )
        messages = self.driver.find_elements(*self.MESSAGES)
        return messages[-1].text if messages else None

    def send_chat(self, message: str):
        self.enter_message(message)
        self.send_message()

    def i_see_us_icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.US_ICON)
        )
        return self.driver.find_element(*self.US_ICON).is_displayed()
    
    def is_message_sent_successully(self):
        return self.i_see_us_icon()


        

