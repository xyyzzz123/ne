from dy import *


def willing(m, n, k, p):
    return (1 - m) * (1 + k * n ** 2) - p


def crowds(steps):
    fig, (crowd, profit, surplus) = plt.subplots(3, figsize=(5, 8))
    crowd.set_ylim(0, 1)
    plt.grid(True)

    i = 0
    mlast = 0
    nlast = 0

    mpai, npai = 0, 0
    ms = 0
    ns = 0

    pai = []
    sps = []
    crd = []
    t = []

    while abs(m - mlast) > 0.001 and i < steps:
        m = f(nlast, i)
        n = g(mlast, i)
        print("m: %.2f, n: %.2f" % (m, n))
        crowd.scatter(i, m, c='b')
        crowd.scatter(i, n, c='r')

        mincrease = m - mlast
        mpai += mincrease * pm(i)
        ms += mincrease * willing(m, n, a, pm(i))

        nincrease = n - nlast
        npai += nincrease * pn(i)
        ns += nincrease * willing(n, m, b, pn(i))

        pai.append(mpai + npai)
        t.append(i)
        sps.append(ms + ns)
        profit.scatter(i, mpai, c='b')
        profit.scatter(i, npai, c='r')
        profit.scatter(i, mpai + npai, c='g')

        surplus.scatter(i, ms, c='b')
        surplus.scatter(i, ns, c='r')
        surplus.scatter(i, ms + ns, c='g')

        mlast = m
        nlast = n

        i += 1

    print(pai[-1])
    profit.plot(t, pai, c='r', alpha=0.7, linestyle='solid')
    plt.show()


def cal_profit(steps):
    i = 0
    mlast, nlast = 0, 0
    pai = 0
    while i < steps:
        m = f(nlast, i)
        n = g(mlast, i)
        pai += (m - mlast) * pm(i) + (n - nlast) * pn(i)
        print("i:%d p:%.2f m:%.2f mlast:%.2f n:%.2f nlast:%.2f" % (i, pm(i), m, mlast, n, nlast))

        mlast, nlast = m, n
        i += 1
    print("profit = %.4f" % (pai))


if __name__ == '__main__':
    # crowds(13)
    cal_profit(13)