from sys import stdin

"https://www.acmicpc.net/problem/15650 N과 M (2) <Silver III>"

def _DFS(arr, at, depth, N, M):
    if depth == M:
        for num in arr:
            print(num, end=' ')
        print()
        return

    for i in range(at, N + 1):
        arr[depth] = i
        _DFS(arr, i + 1, depth + 1, N, M)

def solve_M_and_N(N, M):
    arr = [0 for _ in range(M)]
    _DFS(arr, 1, 0, N, M)

M, N = map(int, stdin.readline().split())
solve_M_and_N(M, N)
