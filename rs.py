import matplotlib.pyplot as plt
import re
import numpy as np


def save_as_dicts():
    label = re.compile("a = ([0-9]+), b = ([0-9]+), steps = ([0-9]+)")
    value = re.compile("[0-9\.]+")

    prices_pattern = re.compile("prices: \[(.*)\]")
    population_pattern = re.compile("population: \[(.*)\]")
    profits_pattern = re.compile("profits: \[(.*)\]")

    prices_dict = {}
    population_dict = {}
    profits_dict = {}

    a, b, s, v, cnt = 0, 0, 0, 0, 0
    with open("./different_steps.txt") as f:
        for line in f.readlines():
            if re.match("{.*}", line): continue

            elif label.match(line):
                a = label.match(line).group(1)
                b = label.match(line).group(2)
                s = label.match(line).group(3)

                prices_dict[(a, b, s, "m")] = []
                prices_dict[(a, b, s, "n")] = []
                population_dict[(a, b, s, "m")] = []
                population_dict[(a, b, s, "n")] = []
                profits_dict[(a, b, s)] = []

                cnt += 1

            elif value.match(line):
                v = value.match(line).group()

            elif prices_pattern.match(line):
                prices_list = prices_pattern.match(line).group(1)
                prices_list = re.findall("\((.+?), (.+?)\)", prices_list)

                for p in prices_list:
                    prices_dict[(a, b, s, "m")].append(float(tuple(p)[0]))
                    prices_dict[(a, b, s, "n")].append(float(tuple(p)[1]))
                print("prices_dict[m]: " + str(prices_dict[(a, b, s, "m")]))

            elif population_pattern.match(line):
                population_list = population_pattern.match(line).group(1)
                population_list = re.findall("\((.+?), (.+?)\)", population_list)

                for p in population_list:
                    population_dict[(a, b, s, "m")].append(float(tuple(p)[0]))
                    population_dict[(a, b, s, "n")].append(float(tuple(p)[1]))
                print("population_dict[m]: " + str(population_dict[(a, b, s, "m")]))

            elif profits_pattern.match(line):
                profits_list = profits_pattern.match(line).group(1).split(", ")

                for p in profits_list:
                    profits_dict[(a, b, s)].append(float(p))
                print("profits_dict: " + str(profits_dict[(a, b, s)]))

            print(line, end="")

    print(cnt)
    return prices_dict, population_dict, profits_dict


def show_result():
    prices_dict, population_dict, profits_dict = save_as_dicts()

    a, b, s = 5, 5, 10

    for s in range(1, 21):
        fig, (price, crowd, profit) = plt.subplots(3, figsize=(5, 8))
        price.grid(True)
        price.set_title("prices")
        price.set_xticks(np.arange(0, s, 1))

        crowd.grid(True)
        crowd.set_title("crowds")
        crowd.set_xticks(np.arange(0, s, 1))

        profit.grid(True)
        profit.set_title("profits")
        profit.set_xticks(np.arange(0, s, 1))

        times = []
        for i in range(s):
            times.append(i)

        print(prices_dict[(str(a), str(b), str(s), "m")])
        price.plot(times, prices_dict[(str(a), str(b), str(s), "m")], c='b', alpha=0.7, linestyle='solid')
        price.plot(times, prices_dict[(str(a), str(b), str(s), "n")], c='r', alpha=0.7, linestyle='solid')
        crowd.plot(times, population_dict[(str(a), str(b), str(s), "m")], c='b', alpha=0.7, linestyle='solid')
        crowd.plot(times, population_dict[(str(a), str(b), str(s), "n")], c='r', alpha=0.7, linestyle='solid')
        profit.plot(times, profits_dict[(str(a), str(b), str(s))], c='g', alpha=0.7, linestyle='solid')
        plt.show()



if __name__ == '__main__':
    show_result()