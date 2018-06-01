from scipy.optimize import minimize

def profit(para, args):
	num = args[0]
	a = args[1]
	b = args[2]
	p = {}
	q = {}
	m = 0.0
	n = 0.0
	pro = 0.0
	for i in range(0, num):
		p[i] = para[2 * i]
		q[i] = para[2 * i + 1]
		p[i] = max(p[i], 0)
		p[i] = min(p[i], 1)
		q[i] = max(q[i], 0)
		q[i] = min(q[i], 1)
		mm = 1 - float(p[i]) / (1 + a * n * n)
		nn = 1 - float(q[i]) / (1 + b * m * m)
		pro += mm * float(p[i]) + nn * float(q[i])
		m = mm
		n = nn
	# print("pro = " + str(pro) + "\n")
	return -pro

N = 20
a = 3.0
b = 6.0
ori = []
ini = [0.14,0.09,0.99,0.99,0.98,0.99,0.86,0.99,0.83,0.98,0.79,0.98,0.79,0.98,0.86,0.98,0.86,0.98,0.79,0.98,0.79,0.98,0.86,0.98,0.86,0.98,0.79,0.98,0.79,0.98,0.86,0.98,0.86,0.98,0.87,0.98,0.98,0.99,0.99,0.99]
bnd = []
for i in range(0, 2 * N):
	ori.append(0.0)
	bnd.append((0, 1))
ori_opt = minimize(profit, ori, args=[N,a,b], method='L-BFGS-B', bounds=bnd)
opt = minimize(profit, ini, args=[N,a,b], method='L-BFGS-B', bounds=bnd)
# for i in range(0, N):
# 	print("(" + str(opt.x[2 * i]) + ", " + str(opt.x[2 * i + 1]) + ")")

print("Oprofit = " + str(-profit(ori_opt.x, [N,a,b])))
print("Wprofit = " + str(-profit([0.14,0.09,0.99,0.99,0.98,0.99,0.86,0.99,0.83,0.98,0.79,0.98,0.79,0.98,0.86,0.98,0.86,0.98,0.79,0.98,0.79,0.98,0.86,0.98,0.86,0.98,0.79,0.98,0.79,0.98,0.86,0.98,0.86,0.98,0.87,0.98,0.98,0.99,0.99,0.99], [N,a,b])))
print("Pprofit = " + str(-profit(opt.x, [N,a,b])))