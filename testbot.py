import sqlite3
import unittest
from unittest.mock import patch, MagicMock

from Hse_bot import start, user_name


class TestStart(unittest.TestCase):

    @patch('Hse_bot.bot.send_message')
    @patch('Hse_bot.bot.register_next_step_handler')
    def test_start(self, mock_register_next_step_handler, mock_send_message):
        message = MagicMock()
        conn = MagicMock()
        cur = MagicMock()

        sqlite3.connect = MagicMock(return_value=conn)
        conn.cursor = MagicMock(return_value=cur)
        cur.execute = MagicMock()
        conn.commit = MagicMock()
        cur.close = MagicMock()
        conn.close = MagicMock()

        start(message)

        assert mock_send_message.call_args_list[0][0][0] == message.chat.id
        assert mock_send_message.call_args_list[0][0][1] == "Привет я бот,который будет присылть тебе гороскоп"
        assert mock_send_message.call_args_list[1][0][0] == message.chat.id
        assert mock_send_message.call_args_list[1][0][1] == "Напиши ,пожалуйста, как тебя зовут?"
        assert mock_register_next_step_handler.call_args_list[0][0][0] == message
        assert mock_register_next_step_handler.call_args_list[0][0][1] == user_name

        assert sqlite3.connect.call_count == 1
        assert conn.cursor.call_count == 1
        assert cur.execute.call_args_list[0][0][
                   0] == 'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), age varchar(50), city varchar(50))'
        assert conn.commit.call_count == 1
        assert cur.close.call_count == 1
        assert conn.close.call_count == 1


unittest.main()