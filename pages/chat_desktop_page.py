# pages/chat_desktop_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class DesktopChatPage(BasePage):
    # לוקייטורים משותפים
    CHAT_INPUT = (By.NAME, "message")
    SEND_BUTTON = (By.XPATH, "//button[@type='submit']")
    SELECT_MODEL_BUTTON = (By.XPATH, "//button[@role='combobox' and normalize-space()='Select model']")
    MODEL_OPTION = (By.XPATH, "//button[normalize-space()='gemma3:1b']")
    MESSAGES = (By.CSS_SELECTOR, ".chat-message")
    US_ICON = (By.XPATH, "//span[text()='US']")
    NEW_CHAT_BUTTON = (By.XPATH, "//div[normalize-space(.)='New chat']")


    # פעולות משותפות
    def enter_message(self, message: str):
        self.wait.until(EC.visibility_of_element_located(self.CHAT_INPUT))
        inp = self.driver.find_element(*self.CHAT_INPUT)
        inp.clear()
        inp.send_keys(message)

    def send_message(self):
        self.wait.until(EC.element_to_be_clickable(self.SEND_BUTTON))
        self.driver.find_element(*self.SEND_BUTTON).click()

    def click_select_model(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_MODEL_BUTTON))
        self.driver.find_element(*self.SELECT_MODEL_BUTTON).click()

    def choose_model_option(self):
        self.wait.until(EC.element_to_be_clickable(self.MODEL_OPTION))
        self.driver.find_element(*self.MODEL_OPTION).click()

    def get_last_message(self):
        self.wait.until(EC.visibility_of_element_located(self.MESSAGES))
        messages = self.driver.find_elements(*self.MESSAGES)
        return messages[-1].text if messages else None

    def i_see_us_icon(self):
        self.wait.until(EC.visibility_of_element_located(self.US_ICON))
        return self.driver.find_element(*self.US_ICON).is_displayed()

    def is_message_sent_successfully(self):
        return self.i_see_us_icon()

    def send_chat(self, message: str):
        self.enter_message(message)
        self.send_message()
