# pages/chat_mobile_page.py
from selenium.webdriver.support import expected_conditions as EC
from .chat_desktop_page import DesktopChatPage

class MobileChatPage(DesktopChatPage):
    """
    אם במובייל כפתור בחירה/שליחה שונה – תוכל להחליף כאן.
    כרגע הוא זהה ל-Desktop. דוגמת override לוגית:
    """

    def send_message(self):
        # אפשר להשאיר כמו בדסקטופ, או לשנות אם דרוש הקלקה אחרת
        super().send_message()
