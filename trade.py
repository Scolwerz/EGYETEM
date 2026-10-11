import random

def main():
    traders = 1000  # futtatott traderek száma

    trade_log = []  # lista a kereskedések logolására
    balance_log = [] # lista a kereskedések logolására
    trade_count_log = [] # lista a kereskedések logolására

    rr = 1.3  # risk-reward ratio
    winrate = 50  # winrate százalékban
    risk = 10

    balance_min = 10
    balance_max = 10000

    success = 0
    blown = 0

    levels = [10, 100]
    for _ in range(500):
        next_value = levels[-1] + (levels[-1] * (risk / 100))
        levels.append(next_value)



    with open("log.txt", "w") as f:
        f.write("\n")

    for trader in range(1, traders + 1):
        #risk = 23  # kockázat százalékban (23%)
        balance = 100  # kezdő balance
        trades = 0  # kereskedések száma egy tradernél

        level = 1

        while balance >= balance_min and balance <= balance_max:  # Kereskedés addig, amíg a balance nem lesz kisebb, mint 10, vagy nagyobb, mint 50,000
            margin = balance * (risk / 100)  # margin a balance alapján

            if random.randint(0, 100) < winrate:
                balance += margin * rr
                trade_log.append("W")
            else:
                balance -= margin
                trade_log.append("L")

            if balance >= levels[level + 1] and balance <= balance_max and risk <= 49:
                level = level + 1
            elif balance <= levels[level - 1] and balance >= balance_min and risk >= 0.5:
                level = level - 1

            trades += 1
            balance_log.append(balance)
            trade_count_log.append(trades)

        if (balance <= balance_min): blown += 1
        elif (balance >= balance_max): success += 1


        with open("log.txt", "a") as f:
            f.write("\n")
            f.write(f"Trader {trader}: {trades} trades ({balance:.2f}$)\n")
            for _ in range(trades):
                if _ % 22 == 0 and _ != 0:
                    f.write("\n")
                f.write(f"{trade_log.pop(0)}[{balance_log.pop(0):.0f}]\t")
            f.write("\n\n")

        trade_log.clear()
        balance_log.clear()

    print(f"WIN: {success}\nLOSS: {blown}\n----------------------------------------")

################################################################
################################################################

if __name__ == "__main__":
    main()
