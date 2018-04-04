import matplotlib.pyplot as plt
import random
import math
from sympy import *

C = 7000
J = 100
M = 2000
N = 400
Pj = 100
Pc = 100


def dc(j, n):
    return max(random.random() * j * n / 1000000 * Pc, 0)
    # if j <= 0: return 0
    # return max(random.random() * math.log10(j) * n, 0)

def dj(c, m):
    return max(random.random() * c * m / 10000000000 * Pj, 0)
    # if c <= 0: return 0
    # return max(random.random() * math.log10(c) * m, 0)


def draw():
    c = C
    j = J
    m = M
    n = N
    fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 6))
    for t in range(1, 1000):
        ax1.scatter(t, c)
        ax2.scatter(t, j)
        print("c: " + str(c) + ", j: " + str(j))
        print("dc: " + str(dc(j, n)) + ", dj: " + str(dj(c, m)))
        print()

        tmp_c = c
        tmp_m = m
        c += dc(j, n)
        m -= dc(j, n)
        j += dj(tmp_c, tmp_m)
        n -= dj(tmp_c, tmp_m)
    plt.show()



def func(Qc, Qj, ecj, ejc, Vc, Vj):
    pc = symbols('pc')
    pj = symbols('pj')

    Dc = map(Function, 'Dc')
    Dj = map(Function, 'Dj')
    Dc = Qc - Qc * pc / Vc
    Dj = Qj - Qj * pj / Vj

    res = solve([Qc * pc + Qc * ecj * pj - Vc * Dc - Vc * ejc * Dj, \
                 Qj * pj + ejc * pc * Qj - Vj * Dj - ecj * Vj * Dc], [pc, pj])
    return res



def res(Qc, Qj, Vc, Vj, ecj, ejc):
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(4, 6))
    pc_list = []
    pj_list = []
    qc_list = []
    qj_list = []
    paic_list = []
    paij_list = []
    pai_list = []

    for i in range(len(ecj)):
        res = func(Qc, Qj, ecj[i], ejc[i], Vc, Vj)
        pc = (list)(res.values())[0]
        pj = (list)(res.values())[1]
        print("pc: " + str((float)(pc)) + " pj: " + str((float)(pj)))
        pc_list.append(pc)
        pj_list.append(pj)

        qc = Qc * (1 - pc / Vc) + ejc[i] * Qj * (1 - pj / Vj)
        qj = Qj * (1 - pj / Vj) + ecj[i] * Qc * (1 - pc / Vc)
        print("qc: " + str((float)(qc)) + " qj: " + str((float)(qj)))
        qc_list.append(qc)
        qj_list.append(qj)

        paic = pc * qc
        paij = pj * pj
        pai = paic + paij
        print("c: " + str((float)(paic)) + " j: " + str((float)(paij)))
        paic_list.append(paic)
        paij_list.append(paij)
        pai_list.append(pai)

        print("pai: " + str((float)(pai)))
        print()

    ax1.plot(ecj, pc_list, c='r', alpha=0.7, linestyle='solid')
    ax1.plot(ecj, pj_list, c='b', alpha=0.7, linestyle='solid')
    ax2.plot(ecj, qc_list, c='r', alpha=0.7, linestyle='solid')
    ax2.plot(ecj, qj_list, c='b', alpha=0.7, linestyle='solid')
    ax3.plot(ecj, paic_list, c='r', alpha=0.7, linestyle='solid')
    ax3.plot(ecj, paij_list, c='b', alpha=0.7, linestyle='solid')
    ax3.plot(ecj, pai_list, c='g', alpha=0.7, linestyle='solid')

    plt.show()



def main():
    draw()

if __name__ == "__main__":
    # func(0, 0, 0, 0, 0, 0)
    Qc = 100 # 100, 10, 10, 60
    Qj = 100
    Vc = 10
    Vj = 10
    # ecj = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    # ejc = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    ecj = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # ejc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # ejc = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    ejc = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
    res(Qc, Qj, Vc, Vj, ecj, ejc)
    # Q()
    # pai()