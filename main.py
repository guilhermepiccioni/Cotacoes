from trades import Trades, SaveTrade


def run():
    td = Trades()
    save_td = SaveTrade()

    try:
        if td:
            print(f"Table Saving: {save_td.save_table()}")
            print(f"Currency Price. {td.hours_update()}\n")
            print(td.create_table())
        else:
            print("Not Found")

    except (Exception, ValueError, KeyError, ImportError, BaseException) as err:
        raise f"-- WARNING: {err}"


if __name__ == "__main__":
    run()
