class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        @functools.lru_cache(None)
        def solve(curr, remain):
            if remain < 0:
                return 0
            elif curr == finish:
                possible = 1
            else:
                possible = 0
            
            for next_loc in range(len(locations)):

                if curr != next_loc:
                    cost = abs(locations[curr]-locations[next_loc])
                    possible += solve(next_loc, remain - cost)
            
            return possible % (10**9+7)

        return solve(start, fuel)