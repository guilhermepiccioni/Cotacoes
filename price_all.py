import requests
import pandas as pd
from datetime import datetime

# FIXME: URL API
request_url = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL")

# FIXME: Date and Hours
date_time_now = datetime.now()
date_screen = date_time_now.strftime('%d/%m/%Y %H:%M')
date_save_excel = date_time_now.strftime('%d_%m_%Y_%H:%M')

# FIXME: Collecting data from api
request_dict = request_url.json()
price_dollar = request_dict["USDBRL"]["bid"]
price_euro = request_dict["EURBRL"]["bid"]
price_btc = request_dict["BTCBRL"]["bid"]
price_lib = request_dict["GBPBRL"]["bid"]

# FIXME: Creating the new table
table = pd.read_excel("Config_tables.xlsx", sheet_name="General")
table.loc[0, "Price"] = float(price_dollar)
table.loc[1, "Price"] = float(price_euro)
table.loc[2, "Price"] = float(price_lib)
table.loc[3, "Price"] = float(price_btc)
table.loc[0, "Last Update Date"] = date_screen
table = table.ffill()

# FIXME: Save database in Excel with pandas
table.to_excel(f"History_price/Cotações|{date_save_excel}|.xlsx", index=False)

# FIXME: Print in screen
print(f"\nCotação Atualizada. {date_screen}\n")
print(table)
