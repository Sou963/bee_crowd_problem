x = int(input())
y = int(input())

start = min(x, y)
end = max(x, y)

total = 0

for i in range(start, end + 1):

    if i % 13 != 0:
        total += i

print(total)