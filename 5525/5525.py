from sys import stdin

"https://www.acmicpc.net/problem/5525 IOIOI <Silver II>"

ioi = int(stdin.readline())
length = int(stdin.readline())
p = stdin.readline()

result = 0
cur = 0
limit = length - ioi * 2
condition = 'I' + 'OI' * ioi
while cur < limit:
    if p[cur] == 'I' and p[cur:cur+2*ioi+1] == condition:
        result += 1
        cur += 2
    else:
        cur += 1

print(result)

