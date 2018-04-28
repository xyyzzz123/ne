

def dp(steps, a, b):
    dp, plist, index = {}, {}, {}
    dp[0] = {0: 0} # m[0] = 0

    for i in range(1, steps + 1):
        dp[i], plist[i], index[i] = {}, {}, {}

        for (k, v) in dp[i - 1].items():
            for j in range(0, 100):
                p = j / 100
                m = 1 - p / (1 + a * k ** 2)
                m = round(m, 4)
                if v + p * (m - k) >= dp[i].get(m, 0):
                    dp[i][m] = round(v + p * (m - k), 4)
                    plist[i][m] = p
                    index[i][m] = k
        print(len(dp[i]))

    max_profit, key = 0, 0
    for (k, v) in dp[steps].items():
        if v >= max_profit:
            max_profit = v
            key = k

    i = steps
    prices, population, profits = [], [], []
    while i > 0:
        prices.append(plist[i][key])
        population.append(key)
        profits.append(dp[i][key])
        key = index[i][key]
        i -= 1
    prices.reverse()
    population.reverse()
    profits.reverse()

    print(max_profit)
    print(prices)
    print(population)
    print(profits)


def dp_mn(steps, a, b):
    dp, plist, index = {}, {}, {}
    dp[0] = {(0, 0): 0}  # dp[step][(m, n)] = max profit at (m, n)
    fw = open("./output.txt", "a")

    for i in range(1, steps + 1):
        dp[i], plist[i], index[i] = {}, {}, {}
        for ((m, n), v) in dp[i - 1].items():

            for j in range(0, 100):
                for k in range(0, 100):
                    pm = j / 100
                    pn = k / 100
                    print("%d (pm, pn) = (%.2f, %.2f)" % (i, pm, pn))

                    mm = round(1 - pm / (1 + a * n ** 2), 2)
                    nn = round(1 - pn / (1 + b * m ** 2), 2)

                    profit = v + (mm - m) * pm + (nn - n) * pn
                    if profit >= dp[i].get((mm, nn), 0):
                        dp[i][(mm, nn)] = round(profit, 2)
                        plist[i][(mm, nn)] = (pm, pn)
                        index[i][(mm, nn)] = (m, n)

        print("i:%d len:%d" % (i, len(dp[i])))
        print(dp[i])

    max_profit = 0
    key = (0, 0)
    for (k, v) in dp[steps].items():
        if v >= max_profit:
            key = k
            max_profit = v

    i = steps
    prices, population, profits = [], [], []
    while i > 0:
        prices.append(plist[i][key])
        population.append(key)
        profits.append(dp[i][key])
        key = index[i][key]
        i -= 1
    prices.reverse()
    population.reverse()
    profits.reverse()

    print(max_profit)
    print("prices: " + str(prices))
    print("population: " + str(population))
    print("profits: " + str(profits))

    fw.write("a = %d, b = %d\n" % (a, b))
    fw.write(str(dp[steps]) + "\n")
    fw.write(str(max_profit) + "\n")
    fw.write("prices: " + str(prices) + "\n")
    fw.write("population: " + str(population) + "\n")
    fw.write("profits: " + str(profits) + "\n\n")
    fw.close()



if __name__ == '__main__':
    steps = 10
    for b in range(1, 11):
        dp_mn(steps, 5, b)

    for a in range(1, 11):
        if a == 5: continue
        for b in range(1, 11):
            dp_mn(steps, a, b)
