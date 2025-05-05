import json
from requests import Response


class ResponseConverter():
    @staticmethod
    def response_my_profile(response: Response):
        # добавить обработку случаев, когда статус код 200 и 400 - вынести ее из common_handlers

        data = json.loads(response.text)
        result = ("Вот информация, которую я о тебе нашел 🤫\n"
                  f"\nИмя: {data['message'][0]['username']} "
                  f"\nМаксимальное количество монеток: {data['message'][0]['coins_collected']} "
                  f"\nЗарегистрирован: {data['message'][0]['joined_at']} ")

        return result
