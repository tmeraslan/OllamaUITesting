# pages/chat_laptop_page.py
from .chat_desktop_page import DesktopChatPage

class LaptopChatPage(DesktopChatPage):
    """
    כרגע משתמש בכל הלוקייטורים של Desktop.
    אם בעתיד תצטרך לוקייטור שונה ללפטופ:
        SEND_BUTTON = (By.XPATH, "...")
        ואז להחליף מתודות שרלוונטיות.
    """
    pass
