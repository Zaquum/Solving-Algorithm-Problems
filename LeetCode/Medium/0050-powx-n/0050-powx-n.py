class Solution:
    def myPow(self, x: float, n: int) -> float:
        @functools.lru_cache(None)
        def solve(x, n):
            if n == 0:
                return 1
            elif n % 2 == 0:
                return solve(x * x, n /2)
            else:
                return x * solve(x * x, (n-1)//2)
        return solve(x,n) if n >= 0 else 1/solve(x,-n)