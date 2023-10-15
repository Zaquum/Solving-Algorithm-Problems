class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        Mod = 10**9 + 7
        # Initialize a memoization table
        memo = {}
        
        def dfs(step, idx):
            # Base cases
            if step == 0 and idx == 0:
                return 1
            elif step == 0 and idx != 0:
                return 0

            if (step, idx) in memo:
                return memo[(step, idx)]

            ans = dfs(step - 1, idx) % Mod
            if idx - 1 >= 0:
                ans += dfs(step - 1, idx - 1) % Mod
            if idx + 1 < arrLen:
                ans += dfs(step - 1, idx + 1) % Mod
       
            memo[(step, idx)] = ans % Mod
            return ans % Mod

        return dfs(steps, 0)