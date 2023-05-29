import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]


class ChatGPT:
    def __init__(self):
        self.context = ""

    def get_response(self, message):
        self.context += message + "\n"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.context,
            max_tokens=100,
            temperature=0.3,
            n=1,
            stop=None,
            timeout=20,
        )
        if response.choices:
            response_text = response.choices[0].text.strip()
            self.context += response_text + "\n"

        return response_text
