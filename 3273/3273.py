from sys import stdin

len_of_seq = int(stdin.readline())
seq = [int(s) for s in stdin.readline().split()]
seq.sort()

start = 0
end = len_of_seq - 1

target = int(stdin.readline())

result = 0
while start < end:
    add = seq[start] + seq[end]

    if add == target:
        result += 1

    if add <= target:
        start += 1

    if add >= target:
        end -= 1

print(result)
