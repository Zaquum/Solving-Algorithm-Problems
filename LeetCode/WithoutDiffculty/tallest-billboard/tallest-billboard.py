class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # choice : left, right, none
        n = len(rods)

        @functools.lru_cache(None)
        def solve(idx, total):
            if idx == n:
                if total == 0:
                    return 0
                return -inf
            return max(
                solve(idx+1, total + rods[idx]) + rods[idx],
                solve(idx+1, total - rods[idx]),
                solve(idx+1, total)
            )
        return solve(0, 0)