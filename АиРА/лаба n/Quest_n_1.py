def go_down(n):
    ways_down = [0] * 21
#    if n == 1:
    ways_down[1] = 1
#    elif n == 2:
    ways_down[2] = 1
#    elif n > 2:
    for i in range(3, n + 1):
        ways_down[i] = ways_down[i - 1] + ways_down[i - 2]
    
    return ways_down[n]

def get_value(first, second):
    while True:
        try:
            user_input = input(f"Сколько этажей в доме от {first} до {second}: ")
            number = int(user_input)

            if first <= number <= second:
                return number
            else:
                print(f"Строители были пьяными и дальше {second} этажа боялись строить")
        except ValueError:
            print(f"Строители не настолько пьяны, попробуйте ещё раз")

building_height = get_value(1, 20)
result = go_down(building_height)
print(f"Спуститься с {building_height} этажа можно {result} способами")