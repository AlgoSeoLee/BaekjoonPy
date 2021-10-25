from sys import stdin

"https://www.acmicpc.net/problem/1599 민식어 <Silver I>"

# N is ng
mansik_char = "a b k d e g h i l m n N o p r s t u w y".split()
mansik_idx = {
    c: idx for c, idx in zip(mansik_char, range(len(mansik_char)))
}

words = []
for _ in range(int(stdin.readline())):
    words.append(stdin.readline().rstrip().replace("ng",'N'))

result = []
for w in words:
    word_idx = tuple(mansik_idx[c] for c in w)
    result.append((word_idx, w))

for _, w in sorted(result):
    print(w.replace('N', "ng"))
