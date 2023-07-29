class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0
        operations = [(100,0),(75,25),(50,50),(25,75)]
        # memo = {}

        def solve(soupA, soupB):
            # return condition
            # if (soupA, soupB) in memo:
            #     return memo[(soupA, soupB)]

            if soupA <= 0 and soupB > 0:
                return 1
            elif soupA <= 0 and soupB <= 0:
                return 0.5
            elif soupA > 0 and soupB <= 0:
                return 0

            ans = 0
            for serve_A, serve_B in operations:
                ans += 0.25 * solve(soupA - serve_A, soupB - serve_B)

            # memo[(soupA, soupB)] = ans  # Store the computed result in memo dict
            return ans
        
        return solve(n, n)