import random

def generate_sorted_array(n):
    return sorted(random.sample(range(n * 10), n))

def binary_search(arr, target):
    low, high, iters = 0, len(arr) - 1, 0
    while low <= high:
        iters += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return iters
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return iters

def interpolation_search(arr, target):
    low, high, iters = 0, len(arr) - 1, 0
    while low <= high and arr[low] <= target <= arr[high]:
        iters += 1
        if arr[high] == arr[low]:
            return iters
        pos = low + (target - arr[low]) * (high - low) // (arr[high] - arr[low])
        if arr[pos] == target:
            return iters
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return iters

for n in [100, 1000, 10000, 100000]:
    arr = generate_sorted_array(n)
    target = random.choice(arr)
    print(f"N={n:>6}  Element tried to find: {target:>7}  Binary: {binary_search(arr, target)}  Interpolate: {interpolation_search(arr, target)}")