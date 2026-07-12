x = int(input())
z = int(input())
while z <= x:
    z = int(input())

total = 0
count = 0
current = x
while total <= z:
    total += current
    current += 1
    count += 1

print(count)