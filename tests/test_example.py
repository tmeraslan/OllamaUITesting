import os
import unittest
from selenium import webdriver
from pages.chat_page import ChatPage


OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:3000')  # Default to localhost if not set

class ExampleTestCase(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()


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