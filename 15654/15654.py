from sys import stdin

def _DFS(cond, arr, at, depth, N, M):
    if depth == M:
        set_of_arr = sorted(set(arr))
        if len(set_of_arr) == M:
            for num in arr:
                print(num, end=' ')
            print()
        return

    for i in range(at, N):
        arr[depth] = cond[i]
        _DFS(cond, arr, 0, depth + 1, N, M)

def solve_M_and_N(cond, N, M):
    arr = [0 for _ in range(M)]
    _DFS(cond, arr, 0, 0, N, M)

M, N = map(int, stdin.readline().split())
cond = sorted(map(int, stdin.readline().split()))
solve_M_and_N(cond, M, N)
