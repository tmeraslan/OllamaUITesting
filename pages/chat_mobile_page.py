# pages/chat_mobile_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .chat_desktop_page import DesktopChatPage

class MobileChatPage(DesktopChatPage):
    SIDEBAR_BUTTON = (By.CSS_SELECTOR, "button[data-state='closed']")

    # מימוש הממשק האחיד: פותח סיידבר במובייל, מחזיר True אם הצליח
    def open_sidebar_if_present(self) -> bool:
        try:
            self.wait.until(EC.element_to_be_clickable(self.SIDEBAR_BUTTON))
            self.driver.find_element(*self.SIDEBAR_BUTTON).click()
            return True
        except (TimeoutException, NoSuchElementException):
            return False
