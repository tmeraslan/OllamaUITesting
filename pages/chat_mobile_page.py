# pages/chat_mobile_page.py
from selenium.webdriver.support import expected_conditions as EC
from .chat_desktop_page import DesktopChatPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class MobileChatPage(DesktopChatPage):
    SIDEBAR_BUTTON = (By.CSS_SELECTOR, "button[data-state='closed']")

    def click_SIDEBAR_BUTTON(self):
        self.wait.until(EC.element_to_be_clickable(self.SIDEBAR_BUTTON))
        self.driver.find_element(*self.SIDEBAR_BUTTON).click()

    

    



