import numpy as np
import matplotlib.pyplot as plt


a = 5
pm = 9 / 10
b = 6
pn = 9 / 10


def one_sided():
    a = 5
    p = 9 / 10
    x = np.arange(0, 1, 0.005)
    y = 1 - p / (1 + a * x**2)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    k = np.arange(0, 1, 0.005)
    n = k
    ax.plot(n, k)

    plt.show()


def f(x):
    return 1 - pm / (1 + a * x ** 2)


def g(x):
    return 1 - pn / (1 + b * x ** 2)


def two_sided():
    fig = plt.figure()
    fig, ax = plt.subplots(1, figsize=(14, 12))
    # ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    n = np.arange(0, 1, 0.005)
    m = 1 - pm / (1 + a * n ** 2)
    ax.plot(n, m)

    m = np.arange(0, 1, 0.005)
    n = 1 - pn / (1 + b * m ** 2)
    ax.plot(n, m)

    plt.show()


def simulate():
    x = 0

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.title('test')
    plt.grid(True)

    n = np.arange(0, 1, 0.005)
    m = 1 - pm / (1 + a * n ** 2)
    ax.plot(n, m)

    m = np.arange(0, 1, 0.005)
    n = 1 - pn / (1 + b * m ** 2)
    ax.plot(n, m)

    i = 0
    while(x != g(f(x))):
        ax.scatter(x, f(x))
        ax.annotate('(%.2f, %.2f)' % (x, f(x)), xy = (x, f(x)), textcoords='data')
        x = f(x)

        ax.scatter(g(x), x)
        ax.annotate('(%.2f, %.2f)' % (g(x), x), xy=(g(x), x), textcoords='data')
        x = g(x)
        print(x)
        i += 1

    print("stop!" + str(x))

    plt.show()



if __name__ == '__main__':
    simulate()
    # two_sided()