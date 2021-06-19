from sys import stdin

"https://www.acmicpc.net/problem/2407 조합 <Silver II>"

DP = {}
def combination(case, select):
    if case == select or select == 0:
        return 1

    result = DP.get((case, select))
    if result != None:
        return result

    result = combination(case - 1, select - 1)
    result += combination(case - 1, select)
    DP[(case, select)] = result
    return result

case, select = map(int, stdin.readline().split())
print(combination(case, select))
