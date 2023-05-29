from nltk.chat.util import Chat
from src.chat_gpt import ChatGPT


class ChatBot:
    def __init__(self):
        self.chatgpt = ChatGPT()
        self.FAREWELL = "Até logo! Tenha um ótimo dia!"
        patterns = [
            (
                r"olá|oi|e aí|oi tudo bem|e aí tudo certo|opa|oiê|salve|oi pessoal|olá pessoal",
                ["Olá! Como posso ajudar?"],
            ),
            (
                r"tchau|adeus|até mais|até logo|até breve|falou|fui|até logo pessoal|até mais tarde|té mais",
                ["Tchau! Tenha um ótimo dia!"],
            ),
            (
                r"obrigado|obrigada|agradecido|grato|valeu|agradeço|agradecimentos|obg|obrigadão|obrigadinho",
                ["De nada! Estou aqui para ajudar."],
            ),
            (
                r"sair|encerrar|finalizar|parar|terminar|cancelar|adeus|despedir|terminar conversa|deixar",
                [self.FAREWELL],
            ),
        ]

        self.chat = Chat(patterns)

    def process_message(self, message: str):
        response = self.chat.respond(message)
        if response:
            return response
        return self.chatgpt.get_response(message)

    def run_chat_bot(self):
        print("Bem-vindo ao Chat Bot!")
        print("Digite 'sair' para encerrar o chat.")

        while True:
            user_input = input("Usuário: ")
            response = self.process_message(user_input)
            print("Chat Bot:", response)
            if response == self.FAREWELL:
                print("Chat encerrado.")
                break
