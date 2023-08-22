import sys
sys.setrecursionlimit(10**6)
def solve(n: int):
    memo = {0:0}
    def dp(n):
        if n in memo:
            return memo[n]
        if n < 0:
            return 2000
        memo[n] = min(dp(n-3), dp(n-5)) + 1
        return memo[n]
    ans = dp(n)
    return ans if ans < 2000 else -1
s = int(input())
print(solve(s))