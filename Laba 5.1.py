lamb = lambda T, p: (A0(T) + A1(T) * p)
A0 = lambda T : 1316 - 5.692*T + 6.83 * 10 ** (-3) * T ** 2
A1 = lambda T : -8.89 * 10 ** (-2) + 4.76 * 10 ** (-3) * T - 5.68 * 10 ** (-7) * T ** 2

for i in range(300 , 360, 10):
    print(f"{int(lamb(i, 2))} {int(lamb(i, 5))} {int(lamb(i, 10))} ")