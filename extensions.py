import json
import requests
from config import *


class ApiException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(iz, to, amount):
        try:
            iz_key = keys[iz]
        except KeyError:
            return ApiException(f'currency {iz} not found')

        try:
            to_key = keys[to]
        except KeyError:
            raise ApiException(f'currency {to} not found')

        if iz_key == to_key:
            raise ApiException(f'impossible to transfer the same currencies {iz}')

        try:
            amount = float(amount)
        except ValueError:
            raise ApiException(f'Value Error {amount}')

        r = requests.get(f'https://api.fastforex.io/convert?from={iz_key}&to={to_key}&amount={amount}&api_key={api}')
        total_base = json.loads(r.content)
        new_price = total_base['result'][to] * float(amount)
        return round(new_price)
