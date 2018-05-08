import numpy as np
import matplotlib.pyplot as plt

# 0 - steps - 1; p0, m0, n0 != 0

a, b = 9, 1


def pm(i):
    # return 0.9
    p = [0.99, 0.99, 0.99, 0.8, 0.99, 0.73, 0.99, 0.99, 0.99, 0.98, 0.98, 0.96, 0.99] # best for 9_1_20
    p = [0.99, 0.99, 0.99, 0.8, 0.99, 0.73, 0.99, 0.99, 0.99, 0.98, 0.98, 0.96, 0.99]
    # p = [0.88, 0.85, 0.9, 0.92, 0.93, 0.94, 0.94, 0.94, 0.93, 0.82, 0.62, 0.5, 0.25]
    # p = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.8, 0.9, 0.9, 0.8, 0.8, 0.5, 0.6]
    # p = [0.98, 0.93, 0.92, 0.96, 0.84, 0.99, 0.98, 0.91, 0.99, 0.87, 0.99, 0.06, 0.01]
    return p[i]


def pn(i):
    # return 0.9
    p = [0.88, 0.66, 0.92, 0.75, 0.93, 0.91, 0.67, 0.6, 0.52, 0.38, 0.22, 0.12, 0.06] # best for 9_1_20
    p = [0.88, 0.66, 0.92, 0.75, 0.93, 0.91, 0.67, 0.6, 0.88, 0.78, 0.89, 0.95, 0.86]
    # p = [0.88, 0.85, 0.9, 0.92, 0.93, 0.94, 0.94, 0.94, 0.93, 0.82, 0.62, 0.5, 0.25]
    # p = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.6, 0.8, 0.9, 0.7, 0.9, 0.6]
    # p = [0.96, 0.88, 0.98, 0.82, 0.99, 0.98, 0.93, 0.97, 0.85, 0.85, 0.61, 0.99, 0.99]
    return p[i]


def f(x, i):
    return 1 - pm(i) / (1 + a * x ** 2)


def g(x, i):
    return 1 - pn(i) / (1 + b * x ** 2)



def one_sided():
    a = 5
    p = 9 / 10
    x = np.arange(0, 1, 0.005)
    y = 1 - p / (1 + a * x ** 2)

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
    fig, ax = plt.subplots(1, figsize=(8, 6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.grid(True)

    n = np.arange(0, 1, 0.005)
    m = 1 - pm(0) / (1 + a * n ** 2)
    ax.plot(n, m)

    m = np.arange(0, 1, 0.005)
    n = 1 - pn(0) / (1 + b * m ** 2)
    ax.plot(n, m)

    plt.show()



def curve(steps):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.grid(True)

    n = np.arange(0, 1, 0.005)
    m = 1 - pm(0) / (1 + a * n ** 2)
    ax.plot(n, m)

    m = np.arange(0, 1, 0.005)
    n = 1 - pn(0) / (1 + b * m ** 2)
    ax.plot(n, m)

    i = 0
    mlast = 0
    nlast = 0
    m = f(nlast, i)
    n = g(mlast, i)

    while abs(m - mlast) > 0.01 and i < steps:
        m, n = f(nlast, i), g(mlast, i)
        print("i: %d, m: %.2f, n: %.2f" % (i, m, n))

        ax.scatter(nlast, m)
        ax.annotate('(%.2f, %.2f)' % (nlast, m), xy=(nlast, m), textcoords='data', fontsize=8)

        ax.scatter(n, mlast)
        ax.annotate('(%.2f, %.2f)' % (n, mlast), xy=(n, mlast), textcoords='data', fontsize=8)

        mlast = m
        nlast = n
        i += 1

    plt.show()


if __name__ == '__main__':
    # curve(13)
    two_sided()
