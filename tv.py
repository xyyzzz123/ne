from dy import *


def crowds():
    x = 0
    i = 0

    mpai = 0
    npai = 0
    mlast = 0
    nlast = 0

    fig, (crowd, profit) = plt.subplots(2, figsize=(8, 6))
    crowd.set_ylim(0, 1)

    plt.grid(True)

    while (abs(x - g(f(x, i), i)) > 0.001):
        crowd.scatter(i, f(x, i), c='b')

        mincrease = f(x, i) - mlast
        mpai += mincrease * pm(i)
        x = f(x, i)
        mlast = x
        print(mincrease)

        crowd.scatter(i, g(x, i), c='r')

        nincrease = g(x, i) - nlast
        # print(nincrease)
        npai += nincrease * pn(i)
        x = g(x, i)
        nlast = x

        profit.scatter(i, mpai, c='b')
        profit.scatter(i, npai, c='r')
        profit.scatter(i, mpai + npai, c='g')

        # print(x)
        i += 1

    print("stop!" + str(x))
    print(mpai)

    plt.show()


if __name__ == '__main__':
    crowds()
