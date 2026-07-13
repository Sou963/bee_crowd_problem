s = 0
numerator = 1
denominator = 1

while numerator <= 39:
    s += numerator / denominator
    numerator += 2
    denominator *= 2

print(f"{s:.2f}")