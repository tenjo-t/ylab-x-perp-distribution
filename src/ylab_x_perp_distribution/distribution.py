from math import sqrt, floor, ceil
import matplotlib.pyplot as plt

tau = (1 + sqrt(5)) / 2
a = 1 / tau
b = 0.01


def f(x):
    return a * x + b


def project_perp(x, y):
    return (y - a * x) * sqrt(1 + a * a) / width


def project_parallel(x, y):
    return (a * y + x) * sqrt(1 + tau * tau) / (1 + tau * a)


width = a + 1
rho = []
seq = []

for i in range(500):
    min = ceil(f(i))
    b_ = b
    b += width
    max = floor(f(i))
    b = b_
    for j in range(min, max + 1):
        rho.append(project_perp(i, j))
        seq.append(project_parallel(i, j))

plt.hist(rho, bins=50)
# plt.scatter(rho, [1] * len(rho))
# plt.scatter(seq, [1] * len(seq))
plt.savefig("hist.png")
