from random import random as rnd
from math import hypot, pi


def monte_carlo_pi(epsilon):
    if epsilon <= 0:
        raise ValueError("epsilon должна быть положительной")

    amount = 0
    cnt = 0
    Pi = 0.0

    while abs(Pi - pi) > epsilon:
        x, y = rnd(), rnd()
        amount += 1

        if hypot(x, y) <= 1.0:
            cnt += 1

        Pi = 4 * cnt / amount

    return Pi, amount


print(f"Точное значение pi: {pi:.10f}\n")
print(f"{'epsilon':>10} {'Оценка pi':>14} {'Ошибка':>14} {'Число точек':>14}")

for epsilon in (10**-1, 10**-2, 10**-3, 10**-4):
    Pi, amount = monte_carlo_pi(epsilon)
    error = abs(Pi - pi)

    print(f"{epsilon:10.4f} {Pi:14.10f} {error:14.10f} {amount:14d}")
    