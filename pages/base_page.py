# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ממשק אחיד: בדסקטופ/לפטופ אין מה לפתוח – נחזיר False
    def open_sidebar_if_present(self) -> bool:
        return False
