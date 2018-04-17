import numpy as np
import matplotlib.pyplot as plt


a = 5
# pm = 95 / 100 # 9 / 10
# pm = 9 / 10
pm = [95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100]
# pm = [9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10]

b = 6
# pn = 95 / 100 # 9 / 10
# pn = 9 / 10
pn = [95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100, 95 / 100]
# pn = [9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10, 9 / 10]

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



def f(x, t):
    return 1 - pm[t] / (1 + a * x ** 2)


def g(x, t):
    return 1 - pn[t] / (1 + b * x ** 2)


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

    # fig = plt.figure()
    fig, (ax, bx) = plt.subplots(2, figsize=(5, 8))

    # ax = fig.add_subplot(1, 1, 1)
    # bx = fig.add_subplot(1, 1, 1)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    bx.set_ylim(0, 1)

    plt.title('test')
    plt.grid(True)

    n = np.arange(0, 1, 0.005)
    m = 1 - pm[0] / (1 + a * n ** 2)
    ax.plot(n, m)

    m = np.arange(0, 1, 0.005)
    n = 1 - pn[0] / (1 + b * m ** 2)
    ax.plot(n, m)

    i = 0
    while(abs(x - g(f(x, i), i)) > 0.001):
        ax.scatter(x, f(x, i))
        bx.scatter(i, f(x, i), c='r')
        ax.annotate('(%.2f, %.2f)' % (x, f(x, i)), xy = (x, f(x, i)), textcoords='data')
        x = f(x, i)

        ax.scatter(g(x, i), x)
        bx.scatter(i, g(x, i), c='b')
        ax.annotate('(%.2f, %.2f)' % (g(x, i), x), xy=(g(x, i), x), textcoords='data')
        x = g(x, i)
        print(x)
        i += 1

    print("stop!" + str(x))

    plt.show()



if __name__ == '__main__':
    simulate()
    # two_sided()
    # one_sided()