import openai


class Chatbot:
    def __init__(self):
        """
        openai.api_key = "[enter your key here]"
        """

    def get_response(self, user_input):
        try:
            bot_response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                max_tokens=2000,
                temperature=0.5,
                messages=[
                    {"role": "system", "content": 'You are a helpful assistant'},
                    {"role": "user", "content": user_input}
                ]
            )

            return bot_response.choices[0].message.content

        except openai.RateLimitError:
            print("Rate limit exceeded.")
            return None


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
