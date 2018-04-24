import numpy as np

a = 5
b = 5


def dp(steps):
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
        if v > max_profit:
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


# def dp_mn(steps):
#     dp, plist, index = {}, {}, {}
#     dp[0] = {(0, 0): 0}  # dp[step][(m, n)] = max profit at (m, n)
#
#     for i in range(1, steps + 1):
#         dp[i], plist[i], index[i] = {}, {}, {}
#
#         for j in range(0, 10):
#             pm = j / 10
#             for k in range(0, 10):
#                 pn = k / 10
#
#                 for ((m, n), v) in dp[i - 1].items():
#                     mm = round(1 - pm / (1 + a * n ** 2), 1)
#                     nn = round(1 - pn / (1 + b * m ** 2), 1)
#
#                     profit = v + (mm - m) * pm + (nn - n) * pn
#                     if profit >= dp[i].get((mm, nn), 0):
#                         dp[i][(mm, nn)] = profit
#                         plist[i][(mm, nn)] = (pm, pn)
#                         index[i][(mm, nn)] = (m, n)
#
#                     dp[i][(mm, nn)] = round(dp[i][(mm, nn)], 4)
#                     print("(%.2f, %.2f): %.4f" % (mm, nn, dp[i][(mm, nn)]))
#
#     max_profit = 0
#     key = (0, 0)
#     for (k, v) in dp[steps].items():
#         if v > max_profit:
#             key = k
#             max_profit = v
#
#     i = steps
#     prices = []
#     while i > 0:
#         prices.append(plist[i][key])
#         key = index[i][key]
#         i -= 1
#     prices.reverse()
#
#     print(max_profit)
#     print(prices)


def dp_mn(steps):
    dp, plist, index = {}, {}, {}
    dp[0] = {(0, 0): 0}  # dp[step][(m, n)] = max profit at (m, n)

    for i in range(1, steps + 1):
        dp[i], plist[i], index[i] = {}, {}, {}
        for ((m, n), v) in dp[i - 1].items():

            for j in range(0, 100):
                pm = j / 100
                for k in range(0, 100):
                    pn = k / 100
                    print("%d (pm, pn) = (%.2f, %.2f)" % (i, pm, pn))
                    mm = round(1 - pm / (1 + a * n ** 2), 2)
                    nn = round(1 - pn / (1 + b * m ** 2), 2)

                    profit = v + (mm - m) * pm + (nn - n) * pn
                    if profit >= dp[i - 1].get((mm, nn), 0):
                        dp[i][(mm, nn)] = round(profit, 2)
                        plist[i][(mm, nn)] = (pm, pn)
                        index[i][(mm, nn)] = (m, n)

        print("i:%d len:%d" % (i, len(dp[i])))
        print(dp[i])

    max_profit = 0
    key = (0, 0)
    for (k, v) in dp[steps].items():
        if v > max_profit:
            key = k
            max_profit = v

    i = steps
    prices, population, profits = [], [], []
    while i > 0:
        prices.append(plist[i][key])
        population.append(index[i][key])
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


if __name__ == '__main__':
    # dp(13)
    # dp(13)
    # l = []
    # l.append({})
    # l[0] = {1:2}
    dp_mn(13)
    # tt = {}
    # tt[(0, 0)] = [2,3]
    # tt[(0, 1)] = tt[(0, 0)].append(1)
    # print(tt)