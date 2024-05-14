class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            
            temp = grid[i][j]
            grid[i][j] = 0
            
            max_gold = 0
            for di, dj in dirs:
                max_gold = max(max_gold, temp + dfs(i + di, j + dj))
            
            grid[i][j] = temp
            
            return max_gold
        
        m = len(grid)
        n = len(grid[0])
        max_gold = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(i, j))
        
        return max_gold