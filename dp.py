import os
import pickle
import matplotlib.pyplot as plt
import numpy as np


def dp(a, b, steps):
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



def dp_mn(a, b, steps):
    dp, plist, index = {}, {}, {}
    dp[0] = {(0, 0): 0}  # dp[step][(m, n)] = max profit at (m, n)
    fw = open("./a_b_s_5_2_.txt", "a")

    for i in range(1, steps + 1):
        dp[i], plist[i], index[i] = {}, {}, {}
        for ((m, n), v) in dp[i - 1].items(): # (0.35, 0.03), 0.2566
            for j in range(0, 100):
                for k in range(0, 100):
                    pm, pn = j / 100, k / 100
                    print("s: %d, i: %d, (pm, pn) = (%.2f, %.2f)" % (steps, i, pm, pn))

                    mm = max(1 - pm / (1 + a * n ** 2), m)
                    nn = max(1 - pn / (1 + b * m ** 2), n)
                    profit = v + (mm - m) * pm + (nn - n) * pn

                    mm, nn = round(mm, 2), round(nn, 2)
                    if profit >= dp[i].get((mm, nn), 0):
                        dp[i][(mm, nn)] = profit
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

    fw.write("a = %d, b = %d, steps = %d\n" % (a, b, steps))
    # fw.write(str(dp[steps]) + "\n")
    fw.write(str(max_profit) + "\n")
    fw.write("prices: " + str(prices) + "\n")
    fw.write("population: " + str(population) + "\n")
    fw.write("profits: " + str(profits) + "\n\n")
    fw.close()



def gen_dp_dict(a, b, steps):
    directory = "./result/%d_%d_%d" % (a, b, steps)
    if not os.path.exists(directory):
        os.makedirs(directory)

    dp, plist, index = {}, {}, {}
    dp[0] = {(0, 0): 0}  # dp[step][(m, n)] = max profit at (m, n)

    for i in range(1, steps + 1):
        dp[i], plist[i], index[i] = {}, {}, {}
        for ((m, n), v) in dp[i - 1].items(): # (0.35, 0.03), 0.2566
            for j in range(0, 100):
                for k in range(0, 100):
                    pm, pn = j / 100, k / 100
                    print("a: %d, b: %d, s: %d, i: %d, (pm, pn) = (%.2f, %.2f)" % (a, b, steps, i, pm, pn))

                    mm = max(1 - pm / (1 + a * n ** 2), m)
                    nn = max(1 - pn / (1 + b * m ** 2), n)
                    profit = v + (mm - m) * pm + (nn - n) * pn

                    mm, nn = round(mm, 2), round(nn, 2)
                    if profit >= dp[i].get((mm, nn), 0):
                        dp[i][(mm, nn)] = profit
                        plist[i][(mm, nn)] = (pm, pn)
                        index[i][(mm, nn)] = (m, n)

        print("i:%d len:%d" % (i, len(dp[i])))
        print(dp[i])

    pickle.dump(dp, open(directory + "/dp.pk", "ab"))
    pickle.dump(plist, open(directory + "/plist.pk", "ab"))
    pickle.dump(index, open(directory + "/index.pk", "ab"))


def process_dp_dict(a, b, s, steps):
    directory = "./result_no_leave/%d_%d_%d" % (a, b, s)
    dp = pickle.load(open(directory + "/dp.pk", "rb"))
    plist = pickle.load(open(directory + "/plist.pk", "rb"))
    index = pickle.load(open(directory + "/index.pk", "rb"))

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
    print(type(profits))



    fig, (price, crowd, profit) = plt.subplots(3, figsize=(5, 8))
    price.grid(True)
    price.set_title("prices")
    price.set_ylim(0, 1)
    price.set_xticks(np.arange(0, steps, 1))

    crowd.grid(True)
    crowd.set_title("crowds")
    crowd.set_ylim(0, 1)
    crowd.set_xticks(np.arange(0, steps, 1))

    profit.grid(True)
    profit.set_title("profits")
    profit.set_ylim(0, 2)
    profit.set_xticks(np.arange(0, steps, 1))

    times = []
    for i in range(steps):
        times.append(i)

    # z = list(zip(*prices))[0]
    # print(z)

    # print(prices[(str(a), str(b), str(s), "m")])
    price.plot(times, list(zip(*prices))[0], c='b', alpha=0.7, linestyle='solid')
    price.plot(times, list(zip(*prices))[1], c='r', alpha=0.7, linestyle='solid')
    crowd.plot(times, list(zip(*population))[0], c='b', alpha=0.7, linestyle='solid')
    crowd.plot(times, list(zip(*population))[1], c='r', alpha=0.7, linestyle='solid')
    profit.plot(times, profits, c='g', alpha=0.7, linestyle='solid')
    plt.show()




if __name__ == '__main__':
    # gen_dp_dict(1, 1, 1)
    # steps = 20
    # for a in range(1, 11):
    #     for b in range(1, 11):
    #         gen_dp_dict(a, b, steps)
    process_dp_dict(1, 1, 20, 13)
    # for s in range(1, 21):
    #     process_dp_dict(1, 1, 20, s)

