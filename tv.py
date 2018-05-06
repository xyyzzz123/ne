from dy import *


def willing(m, n, k, p):
    return (1 - m) * (1 + k * n ** 2) - p


def crowds(steps):
    fig, (crowd, profit, surplus) = plt.subplots(3, figsize=(5, 8))
    crowd.set_ylim(0, 1)
    crowd.set_title("crowd")
    crowd.grid(True)

    profit.set_ylim(0, 1.5)
    profit.set_title("profit")
    profit.grid(True)

    surplus.set_ylim(0, 0.3)
    surplus.set_title("surplus")
    surplus.grid(True)

    i = 0
    mlast = 0
    nlast = 0
    m = f(nlast, i)
    n = g(mlast, i)

    mpai, npai = 0, 0
    msps, nsps = 0, 0
    pai, sps, crd, t = [], [], [], [] # profit, surplus

    while abs(m - mlast) > 0.001 and i < steps:
        print("m: %.2f, n: %.2f" % (m, n))
        crowd.scatter(i, m, c='b', s=14)
        crowd.scatter(i, n, c='r', s=14)

        mincrease = m - mlast
        mpai += mincrease * pm(i)
        msps += mincrease * willing(m, n, a, pm(i))

        nincrease = n - nlast
        npai += nincrease * pn(i)
        nsps += nincrease * willing(n, m, b, pn(i))

        pai.append(mpai + npai)
        t.append(i)
        sps.append(msps + nsps)

        profit.scatter(i, mpai, c='b', s=14)
        profit.scatter(i, npai, c='r', s=14)
        profit.scatter(i, mpai + npai, c='g', s=14)

        surplus.scatter(i, msps, c='b', s=14)
        surplus.scatter(i, nsps, c='r', s=14)
        surplus.scatter(i, msps + nsps, c='g', s=14)

        mlast = m
        nlast = n
        i += 1
        m = f(nlast, i)
        n = g(mlast, i)

    print(pai[-1])
    profit.plot(t, pai, c='g', alpha=0.7, linestyle='solid')
    surplus.plot(t, sps, c='g', alpha=0.7, linestyle='solid')
    plt.show()


def cal_profit(steps):
    i = 0
    mlast, nlast = 0, 0
    pai = 0

    while i < steps:
        m = f(nlast, i)
        n = g(mlast, i)
        pai += (m - mlast) * pm(i) + (n - nlast) * pn(i)
        print("i:%d, p:%.2f, m:%.2f, mlast:%.2f, n:%.2f, nlast:%.2f" % (i, pm(i), m, mlast, n, nlast))

        mlast, nlast = m, n
        i += 1
    print("profit = %.4f" % (pai))


if __name__ == '__main__':
    # crowds(13)
    cal_profit(13)