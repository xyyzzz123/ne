import matplotlib.pyplot as plt
import re
import pickle
import numpy as np

def analysis(filename = "./different_steps.txt", steps = 20):
    label = re.compile("a = ([0-9]+), b = ([0-9]+)")
    value = re.compile("[0-9\.]+")

    prices_pattern = re.compile("prices: \[(.*)\]")
    population_pattern = re.compile("population: \[(.*)\]")
    profits_pattern = re.compile("profits: \[(.*)\]")

    prices_dict = {}
    population_dict = {}
    profits_dict = {}

    a, b, v, cnt = 0, 0, 0, 0
    with open(filename) as f:
        for line in f.readlines():
            if re.match("{.*}", line):
                continue

            elif label.match(line):
                a = label.match(line).group(1)
                b = label.match(line).group(2)

                prices_dict[(a, b, "m")] = []
                prices_dict[(a, b, "n")] = []
                population_dict[(a, b, "m")] = []
                population_dict[(a, b, "n")] = []
                profits_dict[(a, b)] = []

                cnt += 1

            elif value.match(line):
                v = value.match(line).group()

            elif prices_pattern.match(line):
                prices_list = prices_pattern.match(line).group(1)
                prices_list = re.findall("\((.+?), (.+?)\)", prices_list)

                for p in prices_list:
                    prices_dict[(a, b, "m")].append(float(tuple(p)[0]))
                    prices_dict[(a, b, "n")].append(float(tuple(p)[1]))
                print("prices_dict: " + str(prices_dict[(a, b, "m")]))

            elif population_pattern.match(line):
                population_list = population_pattern.match(line).group(1)
                population_list = re.findall("\((.+?), (.+?)\)", population_list)

                for p in population_list:
                    population_dict[(a, b, "m")].append(float(tuple(p)[0]))
                    population_dict[(a, b, "n")].append(float(tuple(p)[1]))
                print("population_dict: " + str(population_dict[(a, b, "m")]))

            elif profits_pattern.match(line):
                profits_list = profits_pattern.match(line).group(1).split(", ")

                for p in profits_list:
                    profits_dict[(a, b)].append(float(p))
                print("profits_dict: " + str(profits_dict[(a, b)]))

            print(line, end="")

    times = []
    for i in range(0, steps):
        times.append(i + 1)
    fig, ax = plt.subplots(1, figsize=(8, 6))
    a = 5
    b = 5
    # for b in range(1, 11):
    #     print(prices_dict[(str(a), str(b), "m")])
    #     ax.plot(times, prices_dict[(str(a), str(b), "m")], c='r', alpha=0.7, linestyle='solid')
    #     ax.plot(times, prices_dict[(str(a), str(b), "n")], c='b', alpha=0.7, linestyle='solid')
    ax.plot(times, prices_dict[str(a), str(b), "m"], c='r', label=u"$y = sin(x)$")
    ax.plot(times, prices_dict[str(a), str(b), "n"], c='b', label=b)
    plt.show()


def save_as_dicts():
    label = re.compile("a = ([0-9]+), b = ([0-9]+)")
    value = re.compile("[0-9\.]+")

    prices_pattern = re.compile("prices: \[(.*)\]")
    population_pattern = re.compile("population: \[(.*)\]")
    profits_pattern = re.compile("profits: \[(.*)\]")

    prices_dict = {}
    population_dict = {}
    profits_dict = {}

    a, b, v, cnt = 0, 0, 0, 0
    with open("./output.txt") as f:
        for line in f.readlines():
            if re.match("{.*}", line): continue

            elif label.match(line):
                a = label.match(line).group(1)
                b = label.match(line).group(2)

                prices_dict[(a, b, "m")] = []
                prices_dict[(a, b, "n")] = []
                population_dict[(a, b, "m")] = []
                population_dict[(a, b, "n")] = []
                profits_dict[(a, b)] = []

                cnt += 1

            elif value.match(line):
                v = value.match(line).group()

            elif prices_pattern.match(line):
                prices_list = prices_pattern.match(line).group(1)
                prices_list = re.findall("\((.+?), (.+?)\)", prices_list)

                for p in prices_list:
                    prices_dict[(a, b, "m")].append(float(tuple(p)[0]))
                    prices_dict[(a, b, "n")].append(float(tuple(p)[1]))
                print("prices_dict: " + str(prices_dict[(a, b, "m")]))

            elif population_pattern.match(line):
                population_list = population_pattern.match(line).group(1)
                population_list = re.findall("\((.+?), (.+?)\)", population_list)

                for p in population_list:
                    population_dict[(a, b, "m")].append(float(tuple(p)[0]))
                    population_dict[(a, b, "n")].append(float(tuple(p)[1]))
                print("population_dict: " + str(population_dict[(a, b, "m")]))

            elif profits_pattern.match(line):
                profits_list = profits_pattern.match(line).group(1).split(", ")

                for p in profits_list:
                    profits_dict[(a, b)].append(float(p))
                print("profits_dict: " + str(profits_dict[(a, b)]))


            print(line, end="")

    print(cnt)
    pickle.dump(prices_dict, open("./prices_dict.pk", "wb"))
    pickle.dump(population_dict, open("./population_dict.pk", "wb"))
    pickle.dump(profits_dict, open("./profits_dict.pk", "wb"))

def show_prices():
    times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    prices_dict = pickle.load(open("./prices_dict.pk", "rb"))
    fig, ax = plt.subplots(1, figsize=(8, 6))
    a = 5
    b = 5
    # for b in range(1, 11):
    #     print(prices_dict[(str(a), str(b), "m")])
    #     ax.plot(times, prices_dict[(str(a), str(b), "m")], c='r', alpha=0.7, linestyle='solid')
    #     ax.plot(times, prices_dict[(str(a), str(b), "n")], c='b', alpha=0.7, linestyle='solid')
    ax.plot(times, prices_dict[str(a), str(b), "m"], c='r', label=u"$y = sin(x)$")
    ax.plot(times, prices_dict[str(a), str(b), "n"], c='b', label=b)
    plt.show()

def test():
    p = [0.95, 0.95, 0.96, 0.94, 0.95, 0.87, 0.82, 0.74, 0.57, 0.55, 0.44, 0.21, 0.21]
    times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    fig, ax = plt.subplots(1, figsize=(8, 6))
    ax.plot(times, p)
    plt.show()



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



    # fig, (price, crowd, profit) = plt.subplots(3, figsize=(5, 8))
    plt.figure(figsize=(14, 4))
    price, crowd, profit = plt.subplot(131), plt.subplot(132), plt.subplot(133)

    price.set_title("prices")
    price.set_ylim(0, 1)
    price.set_xticks(np.arange(0, steps, 1))

    # crowd.grid(True)
    crowd.set_title("crowds")
    crowd.set_ylim(0, 1)
    crowd.set_xticks(np.arange(0, steps, 1))

    # profit.grid(True)
    profit.set_title("profits")
    profit.set_ylim(0, 2)
    profit.set_xticks(np.arange(0, steps, 1))

    times = []
    for i in range(steps):
        times.append(i)

    # z = list(zip(*prices))[0]
    # print(z)

    # print(prices[(str(a), str(b), str(s), "m")])
    price.plot(times, list(zip(*prices))[0], c='r', alpha=0.7, linestyle='solid')
    price.plot(times, list(zip(*prices))[1], c='b', alpha=0.7, linestyle='solid')
    crowd.plot(times, list(zip(*population))[0], c='r', alpha=0.7, linestyle='solid')
    crowd.plot(times, list(zip(*population))[1], c='b', alpha=0.7, linestyle='solid')
    profit.plot(times, profits, c='g', alpha=0.7, linestyle='solid')
    plt.show()


if __name__ == '__main__':
    # save_as_dicts()
    # show_prices()
    # analysis()
    # process_dp_dict(8, 10, 20, 20)
    for b in range(1, 11):
        process_dp_dict(2, b, 20, 20)