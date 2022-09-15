import requests

from Models.constants import CONSTANT


class Trades:
    Const = CONSTANT

    def __init__(self):
        self.url = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL")

    def refactoring_hours(self):
        date_time_now = self.Const.date_time_now
        return date_time_now.strftime('%d_%m_%Y_%H:%M')

    def create_table(self):
        table = self.Const.table
        table.loc[0, "Price"] = float(self.Const.price_dollar)
        table.loc[1, "Price"] = float(self.Const.price_euro)
        table.loc[2, "Price"] = float(self.Const.price_lib)
        table.loc[3, "Price"] = float(self.Const.price_btc)
        table.loc[0, "Last Update Date"] = self.refactoring_hours()
        return table.ffill()


class SaveTrade:
    Td = Trades()

    def save_table(self):
        c_t = self.Td.create_table()
        h_u = self.Td.refactoring_hours()

        c_t.to_excel(
            f"History_price/Trades|{h_u}|.xlsx",
            index=False
        )
        return "Saved Successfully"
