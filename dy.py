import numpy as np
import matplotlib.pyplot as plt


a = 5
# pm = 9 / 10
b = 6
# pn = 9 / 10


def pm(i):
    return 0.01


def pn(i):
    return 0.01


def f(x, i):
    return 1 - pm(i) / (1 + a * x ** 2)


def g(x, i):
    return 1 - pn(i) / (1 + b * x ** 2)



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


def two_sided():
    fig = plt.figure()
    fig, ax = plt.subplots(1, figsize=(14, 12))
    # ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    n = np.arange(0, 1, 0.005)
    m = 1 - pm(0) / (1 + a * n ** 2)
    ax.plot(n, m)

    m = np.arange(0, 1, 0.005)
    n = 1 - pn(0) / (1 + b * m ** 2)
    ax.plot(n, m)

    plt.show()


def curve():
    x = 0

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.title('test')
    plt.grid(True)

    n = np.arange(0, 1, 0.005)
    m = 1 - pm(0) / (1 + a * n ** 2)
    ax.plot(n, m)

    m = np.arange(0, 1, 0.005)
    n = 1 - pn(0) / (1 + b * m ** 2)
    ax.plot(n, m)

    i = 0
    while(x != g(f(x, i), i)):
        ax.scatter(x, f(x, i))
        ax.annotate('(%.2f, %.2f)' % (x, f(x, i)), xy = (x, f(x, i)), textcoords='data')
        x = f(x, i)

        ax.scatter(g(x, i), x)
        ax.annotate('(%.2f, %.2f)' % (g(x, i), x), xy=(g(x, i), x), textcoords='data')
        x = g(x, i)
        print(x)
        i += 1

    print("stop!" + str(x))

    plt.show()



if __name__ == '__main__':
    curve()
    # two_sided()
