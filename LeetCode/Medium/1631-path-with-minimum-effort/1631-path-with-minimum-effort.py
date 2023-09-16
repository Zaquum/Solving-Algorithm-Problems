class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        row = len(heights)
        col = len(heights[0])
        
        def is_valid(x,y,visited):
            return 0<=x<row and 0<=y<col and not visited[x][y]

        def dfs(x,y, max_effort, visited):
            if x == row-1 and y == col - 1:
                return True
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if is_valid(nx,ny, visited) and abs(heights[x][y]-heights[nx][ny])<=max_effort:
                    if dfs(nx,ny, max_effort, visited):
                        return True
            return False

        left = 0
        right = 0
        for i in range(row):
            for j in range(col):
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if ni >= row or nj >= col or ni < 0 or nj < 0:
                        continue
                    right = max(right, abs(heights[i][j] - heights[ni][nj]))
        while left <= right:
            mid = (left + right) // 2
            visited = [[False] * col for _ in range(row)]
            if dfs(0,0, mid, visited):
                right = mid - 1
            else:
                left = mid + 1
        return left