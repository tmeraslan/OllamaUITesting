# tests/test_new_chat.py
import unittest
import os
from drivers.driver_factory import get_driver
from pages.page_factory import PageFactory

OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:3000')

def is_mobile_env() -> bool:
    res = os.getenv("RESOLUTION", "").lower()
    if res:
        return res.startswith("mobile")
    w = int(os.getenv("SCREEN_WIDTH", "1920"))
    h = int(os.getenv("SCREEN_HEIGHT", "1080"))
    return w <= 414 and h <= 896

class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_unified_chat_flow(self):
        self.driver.get(OLLAMA_URL)
        chat = PageFactory.create_chat_page(self.driver)
        # chat.click_select_model()
        # chat.choose_model_option()
        if is_mobile_env():
            opened = chat.open_sidebar_if_present()

        chat.send_chat("Hello from unified test!")
        self.assertTrue(chat.is_message_sent_successfully())




