def binary_search(f, x_left, x_right, epsilon=1e-6):
    if epsilon <= 0:
        print("эпсилон должен быть положительным")
        return

    if x_left >= x_right:
        print("Левая граница должна быть меньше правой")
        return
    
    f_left = f(x_left)
    f_right = f(x_right)

    if f_left == 0:
        return x_left
    if f_right == 0:
        return x_right

    if f_left * f_right > 0:
        print("На концах отрезка должны быть разные знаки")
        return
    
    increasing = f_left < f_right


    while (x_right - x_left) / 2 > epsilon:
        x_middle = (x_left + x_right) / 2
        f_middle = f(x_middle)

        if f_middle == 0:
            return x_middle

        if increasing:
            if f_middle < 0:
                x_left = x_middle
            else:
                x_right = x_middle
        else:
            if f_middle > 0:
                x_left = x_middle
            else:
                x_right = x_middle

    return (x_left + x_right) / 2


epsilon = 10**-6


def raising_f(x):
    return x**3 - x - 2


root = binary_search(raising_f, 1.0, 2.0, epsilon)
print(f"Возрастающая функция: x = {root:.8f}")
print(f"Значение функции: {raising_f(root):.8f}")



def lowering_f(x):
    return 2 - x**3


root = binary_search(lowering_f, -10.0, 10.0, epsilon)
print(f"Убывающая функция: x = {root:.8f}")
print(f"Значение функции: {lowering_f(root):.8f}")