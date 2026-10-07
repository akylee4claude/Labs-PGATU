def steps_counter(n, k):
    step_matrix = [[0] * (n + k + 2) for i in range(k + 1)]
    step_matrix[0][n] = 1
    for i in range(1, k + 1):
        for j in range(1, n + k + 1):
            step_matrix[i][j] = step_matrix[i-1][j-1] + step_matrix[i-1][j+1]               
    return step_matrix[k-1][1]

def get_value(first, second):
    while True:
        try:
            print("Введите через пробел расстояние от магазина до человека и кол-во шагов: ")
            user_input = input(f"Учтите что данные вводятся в диапозоне от {first} до {second} и расстояние не может превышать кол-во шагов: ")
            n, k = map(int, user_input.split())
            
            if first <= n <= second:
                if first <= n <= k:
                    return n, k
                else:
                    print("У нас человвек а не сороконожка")
            else:
                print("Человек не дошйдет до магазина")

        except ValueError:
            print("Не играйте с чувствами человека")

n, k = get_value(1, 16)
result = steps_counter(n, k)
print(f"кол-во вариантов: {result}")