import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]


class ChatGPT:
    def __init__(self):
        self.context = ""

    def get_response(self, message: str):
        self.context += f"{message} \n"

        response = openai.Completion.create(
            engine=os.environ.get("OPENAI_ENGINE", "text-davinci-003"),
            prompt=self.context,
            max_tokens=int(os.environ.get("OPENAI_MAX_TOKENS", 100)),
            temperature=float(os.environ.get("OPENAI_TEMPERATURE", 0.3)),
            n=int(os.environ.get("OPENAI_N", 1)),
            stop=os.environ.get("OPENAI_STOP", None),
            timeout=int(os.environ.get("OPENAI_TIMEOUT", 20)),
        )
        if response.choices:
            response_text = response.choices[0].text.strip()
            self.context += f"{response_text} \n"

        return response_text
