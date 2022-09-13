import requests
import pandas as pd

from datetime import datetime


class _Const:
    request_url = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL")
    table = pd.read_excel("Config_tables.xlsx", sheet_name="General")

    request_dict = request_url.json()
    price_dollar = request_dict["USDBRL"]["bid"]
    price_euro = request_dict["EURBRL"]["bid"]
    price_btc = request_dict["BTCBRL"]["bid"]
    price_lib = request_dict["GBPBRL"]["bid"]

    date_time_now = datetime.now()


CONSTANT = _Const()
