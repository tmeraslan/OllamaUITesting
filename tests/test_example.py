# # tests/test_example.py
# import unittest
# import os
# from drivers.driver_factory import get_driver
# # from pages.chat_page import ChatPage
# from pages.page_factory import PageFactory 

# OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:3000')

# class ExampleTestCase(unittest.TestCase):
#     def setUp(self):
#         self.driver = get_driver()   # ← שימוש ב-DriverFactory דרך get_driver

#     def tearDown(self):
#         self.driver.quit()

#     def test_sent_message(self):
#         self.driver.get(OLLAMA_URL)
#         chat = PageFactory.create_chat_page(self.driver)
#         chat.click_select_model()
#         chat.choose_model_option()
#         chat.send_chat("Hello, Ollama!")
#         self.assertTrue(chat.is_message_sent_successfully())
