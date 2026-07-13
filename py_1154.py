total = 0
count = 0
while True:
    age = int(input())
    if age < 0:
        break

    total += age
    count += 1

average = total / count
print(f"{average:.2f}")