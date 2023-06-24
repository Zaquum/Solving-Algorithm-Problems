class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # choice : left, right, none
        n = len(rods)

        @functools.lru_cache(None)
        def solve(idx, diff):
            if idx == n:
                if diff == 0:
                    return 0
                return float('-inf')
            return max(
                solve(idx+1, diff + rods[idx]) + rods[idx], # left
                solve(idx+1, diff - rods[idx]), # right
                solve(idx+1, diff) # None
            )
        return solve(0, 0)