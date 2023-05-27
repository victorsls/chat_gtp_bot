import pytest
from unittest import mock
from src.chat_bot import ChatBot

@pytest.fixture
def chat_bot():
    return ChatBot()

def test_process_message_with_auto_response(chat_bot):
    message = "oi"
    expected_response = "Olá! Como posso ajudar?"
    response = chat_bot.process_message(message)
    assert response == expected_response

def test_process_message_with_gpt_response(chat_bot):
    message = "Qual é o clima hoje?"
    expected_response = "Exemplo de resposta do ChatGPT"
    with mock.patch("src.chat_bot.ChatGPT.get_response") as mock_get_response:
        mock_get_response.return_value = expected_response
        response = chat_bot.process_message(message)
        assert response == expected_response

def test_run_chat_bot_with_exit(chat_bot, capsys):
    user_input = "sair"
    expected_output = "Chat encerrado."

    with mock.patch("builtins.input", side_effect=[user_input]):
        chat_bot.run_chat_bot()

    captured = capsys.readouterr()
    assert expected_output in captured.out

def test_run_chat_bot_with_response(chat_bot, capsys):
    user_input = "Qual é o seu nome?"
    expected_output = "Chat Bot: Exemplo de resposta"

    with mock.patch("builtins.input", side_effect=[user_input, "sair"]):
        with mock.patch("src.chat_bot.ChatGPT.get_response") as mock_get_response:
            mock_get_response.return_value = "Exemplo de resposta"
            chat_bot.run_chat_bot()

    captured = capsys.readouterr()
    assert expected_output in captured.out
