from sys import stdin

"https://www.acmicpc.net/problem/9935 문자열 폭발 <Gold IV>"

plain = stdin.readline().rstrip()
bomb = stdin.readline().rstrip()
bomb_length = len(bomb)

result = [' ']
result_idx = 0
for c in plain:
    result[result_idx] = c
    result.append(' ')
    result_idx += 1
    if result[result_idx - 1] == bomb[bomb_length-1]:
        explode = True
        for j in range(bomb_length):
            if result[result_idx-1-j] != bomb[bomb_length-1-j]:
                explode = False
                break

        if explode:
            result_idx = result_idx - bomb_length

result = ''.join(result[0:result_idx])
if result == '':
    print("FRULA")
else:
    print(result)
