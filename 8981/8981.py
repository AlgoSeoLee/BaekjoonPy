from sys import stdin

N = int(stdin.readline())
array = list(map(int, stdin.readline().split()))

position = 0
count = 0
result = [0 for _ in range(N)]

while count < N:
    while result[position] != 0:
        position = (position + 1) % N

    value = array[count]
    count += 1
    result[position] = value
    position = (position + value) % N

print(N)
print(*result)

