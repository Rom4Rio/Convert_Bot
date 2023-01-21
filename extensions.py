import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConvertor:
    @staticmethod
    def convert(base: str, quote: str, amount:str):
        if base == quote:
            raise ConvertionException(f'Невозможно перевести {base} в {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Валюта {base} не найдена!")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Валюта {quote} не найдена!")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f"https://v6.exchangerate-api.com/v6/bf82f6eaf743dd359a9cbaf9/pair/{base_ticker}/{quote_ticker}")
        total_base = json.loads(r.content)
        print(total_base)
        new_price = total_base['conversion_rate'] * amount
        new_price = round(new_price, 3)
        message = f"Цена {amount} {base} в {quote} : {new_price}"
        return message
