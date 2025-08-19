# tests/test_example.py
import os
import unittest
from selenium import webdriver
from pages.chat_page import ChatPage
from selenium.webdriver.chrome.options import Options
import shutil
import tempfile



OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:3000')  # Default to localhost if not set

class ExampleTestCase(unittest.TestCase):
    
    
    def setUp(self):
        options = Options()
        if os.getenv("HEADLESS", "false").lower() == "true":
            options.add_argument("--headless=new")
            

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # # Create a temporary profile folder -user data
        self.user_data_dir = tempfile.mkdtemp(prefix=f"chrome-user-data-uid-{time.time()}")
        options.add_argument(f"--user-data-dir={self.user_data_dir}")

        # # It's important to add the window-size before creating the driver
        
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()
        shutil.rmtree(self.user_data_dir, ignore_errors=True)


    def test_sent_message(self):
        self.driver.get(OLLAMA_URL)
        chat = ChatPage(self.driver)
        chat.click_select_model()
        chat.choose_model_option()
        chat.send_chat("Hello, Ollama!")
        self.assertTrue(chat.is_message_sent_successully())
        self.driver.quit()





if __name__ == '__main__':
    unittest.main()