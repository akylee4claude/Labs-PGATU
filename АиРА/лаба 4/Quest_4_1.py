number = int(input())
weights = list(map(int, input().split()))
total = sum(weights)

sums = [0]

for w in weights:
    new_sums = []
    for s in sums:
        new_sums.append(s)
        new_sums.append(s + w)
    sums = new_sums

best = total

for a in sums:
    diff = abs(2 * a - total)
    if diff < best:
        best = diff

print(best)