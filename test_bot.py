import unittest
from unittest.mock import patch
from Hse_bot import start, user_name, agee, cityy, types


class TestBot(unittest.TestCase):

    @patch('Hse_bot.TeleBot.send_message')
    def test_start_command(self, mock_send_message):
        message = types.Message()
        message.chat.id = 'chat_id_1'
        start(message)
        mock_send_message.assert_called_once_with('chat_id_1', 'Привет я бот,который будет присылть тебе гороскоп')
        mock_send_message.assert_called_with('chat_id_1', 'Напиши ,пожалуйста, как тебя зовут?')
        self.assertEqual(message.text.strip(), 'привет')

    @patch('Hse_bot.TeleBot.send_message')
    def test_user_name(self, mock_send_message):
        message = types.Message()
        message.text = 'John'
        user_name(message)
        mock_send_message.assert_called_once_with('chat_id_1', 'А теперь подскажи мне свой возраст, John?')

    @patch('Hse_bot.TeleBot.send_message')
    def test_agee(self, mock_send_message):
        message = types.Message()
        message.text = '25'
        agee(message)
        mock_send_message.assert_called_once_with('chat_id_1', 'А теперь подскажи мне,где ты живешь John в свои 25?')

    @patch('Hse_bot.TeleBot.send_message')
    def test_cityy(self, mock_send_message):
        message = types.Message()
        message.text = 'Moscow'
        cityy(message)
        mock_send_message.assert_called_once_with('chat_id_1', 'Выбери свой знак зодиака')


if __name__ == '__main__':
    unittest.main()