class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        
        def dfs(i, j, visited, golds):
            # recursion exit
            if i < 0 or i >= m or j < 0 or j >= n:
                return golds
            if grid[i][j] == 0:
                return golds
            

            visited.add((i, j))
            golds += grid[i][j]
            tmp = 0
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if (ni, nj) in visited:
                    continue
                tmp = max(tmp, dfs(ni, nj, visited, golds))
            visited.remove((i,j))
            return tmp
        
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                ans = max(ans, dfs(i,j, set(), 0))
                # print(ans)
        return ans