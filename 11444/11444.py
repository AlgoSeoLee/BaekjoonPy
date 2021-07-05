from sys import stdin

MOD = 1000000007
dp = {}

def fibo(times):
    if times <= 0:
        return 0
    elif times <= 2:
        return 1

    result = dp.get(times)
    if result != None:
        return result

    if times % 2 != 1:
        mid = (times + 1) / 2
        tmp1 = fibo(mid)
        tmp2 = fibo(mid+1)
        result = tmp1 * tmp1
        result += tmp2 * tmp2
    else:
        mid = times / 2
        tmp1 = fibo(mid - 1)
        tmp2 = fibo(mid)
        result = 2 * tmp1 + tmp2
        result *= tmp2

    result %= MOD
    dp[times] = result
    return result

print(fibo(int(stdin.readline())))
