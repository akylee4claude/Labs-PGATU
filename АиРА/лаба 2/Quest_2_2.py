def step_counter(k, n):
    step_list = [0] * (n+1)
    step_list[0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i - j >= 0:
                step_list[i] = step_list[i] + step_list[i-j]
    return step_list[n]

def get_value(first, second):
    while True:
        try:
            user_input = input(f"Введите через пробел максимальный прыжок {first} и кол-во ступеней {second}: ")
            k, n = map(int, user_input.split())
            
            if first <= n <= second:
                if first <= k <= n:
                    return k, n
                else:
                    print(f"От кролика осталась красная лужица в стене")
            else:
                print(f"Кролик умер от усталости")
   
        except ValueError:
            print(f"У кролика есть чувства")

k, n = get_value(1, 50)
result = step_counter(k, n)
print(f"Кролик прыгал {result} разными способами")
