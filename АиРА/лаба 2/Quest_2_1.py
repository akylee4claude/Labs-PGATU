def f_counter(n):
    f_list = [0] * 73

    f_list[1] = 1
    f_list[2] = 1

    for i in range(3, n + 1):
        f_list[i] = f_list[i - 1] + f_list[i - 2]
    
    return f_list[n]

def get_value(first, second):
    while True:
        try:
            user_input = input(f"Введите порядковый номер числа Фибоначчи от {first} до {second}: ")
            number = int(user_input)

            if first <= number <= second:
                return number
            else:
                print(f"Дальше {second} не надо")
        except ValueError:
            print(f"Порядковый номер, но не что-то другое")

f_max = get_value(1, 72)
result = f_counter(f_max)
print(f"Порядковый номер {f_max}, Число Фибоначчи  {result} ")