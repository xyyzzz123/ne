import matplotlib.pyplot as plt
import re
import pickle

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
    # a = 2
    # for b in range(1, 11):
    #     print(prices_dict[(str(a), str(b), "m")])
    #     ax.plot(times, prices_dict[(str(a), str(b), "m")], c='r', alpha=0.7, linestyle='solid')
    #     ax.plot(times, prices_dict[(str(a), str(b), "n")], c='b', alpha=0.7, linestyle='solid')
    ax.plot(times, prices_dict["5", "5", "m"])
    plt.show()

def test():
    p = [0.95, 0.95, 0.96, 0.94, 0.95, 0.87, 0.82, 0.74, 0.57, 0.55, 0.44, 0.21, 0.21]
    times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    fig, ax = plt.subplots(1, figsize=(8, 6))
    ax.plot(times, p)
    plt.show()

if __name__ == '__main__':
    # save_as_dicts()
    show_prices()
    test()