class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # DFS : Time limit
        # moved = [0]
        # remain = [0]
        
        directions = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]
        @functools.lru_cache(None)
        def dfs(k, row, column):
            if row >= n or column >= n or row <0 or column < 0:
                return 0
            elif k == 0:
                # if row < n and column < n:
                return 1
            # moved[0] += 1
            else:
                result = 0
                for dy, dx in directions:
                    result += dfs(k - 1, row + dy, column + dx)
                return result/8
        return dfs(k, row, column)