import pytest
from unittest import mock
from src.chat_gpt import ChatGPT


@pytest.fixture
def chat_gpt():
    return ChatGPT()


def test_get_response(chat_gpt):
    message = "Qual é o clima hoje?"
    expected_response = "A previsão do tempo para hoje é ensolarado."

    with mock.patch("src.chat_gpt.openai.Completion.create") as mock_create:
        mock_create.return_value.choices[0].text.strip.return_value = expected_response
        response = chat_gpt.get_response(message)

    assert response == expected_response


def test_get_response_with_empty_context(chat_gpt):
    message = "Olá!"
    expected_response = "Olá! Como posso ajudar?"

    with mock.patch("src.chat_gpt.openai.Completion.create") as mock_create:
        mock_create.return_value.choices[0].text.strip.return_value = expected_response
        response = chat_gpt.get_response(message)

    assert response == expected_response
