# pages/page_factory.py
import os

from .chat_desktop_page import DesktopChatPage
from .chat_laptop_page import LaptopChatPage
from .chat_mobile_page import MobileChatPage

class PageFactory:
    @staticmethod
    def create_chat_page(driver):
        # עדיף להעביר RESOLUTION מה-matrix: desktop-full / laptop / mobile
        res_name = os.getenv("RESOLUTION", "").lower()

        if not res_name:
            # fallback לפי גודל המסך
            w = int(os.getenv("SCREEN_WIDTH", "1920"))
            h = int(os.getenv("SCREEN_HEIGHT", "1080"))
            if w <= 414 and h <= 896:
                res_name = "mobile"
            elif w <= 1366:
                res_name = "laptop"
            else:
                res_name = "desktop-full"

        if res_name.startswith("mobile"):
            return MobileChatPage(driver)
        elif res_name.startswith("laptop"):
            return LaptopChatPage(driver)
        else:
            # ברירת מחדל: desktop
            return DesktopChatPage(driver)
