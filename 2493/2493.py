from sys import stdin

"https://www.acmicpc.net/problem/2493 탑 <Gold V>"

num_of_tower = int(stdin.readline())
towers = [int(v) for v in stdin.readline().split()]

received = [0 for _ in range(num_of_tower)]
unreceive = []
for index in range(num_of_tower - 1, -1, -1):
    current = towers[index]
    while unreceive:
        start_index = unreceive.pop()
        start = towers[start_index]
        if current > start:
            received[start_index] = index + 1
        else:
            unreceive.append(start_index)
            break

    unreceive.append(index)

for to in received:
    print(to, end=" ")
print()

