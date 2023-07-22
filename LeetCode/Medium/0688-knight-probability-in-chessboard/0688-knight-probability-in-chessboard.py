class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        directions = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]

        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1
        
        for step in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for dy, dx in directions:
                        ni, nj = i + dy, j + dx
                        if 0 <= ni < n and 0 <= nj < n:
                            dp[step][i][j] += dp[step - 1][ni][nj] / 8.0
        
        return sum(sum(row) for row in dp[k])
        # DFS : Time limit
        # moved = [0]
        # remain = [0]
        
        # directions = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]
    
        # def dfs(k, row, column, off):
        #     if row >= n or column >= n or row <0 or column < 0:
        #         off = 1
        #     if k == 0:
        #         # if row < n and column < n:
        #         moved[0] += 1
        #         if off == 0 and 0<=row<n and 0<=column<n:
        #             remain[0] += 1
        #         return
        #     # moved[0] += 1
        #     for dy, dx in directions:
        #         dfs(k - 1, row + dy, column + dx, off)

        # dfs(k, row, column, 0)

        # # print(moved[0])
        # # print(remain[0])
        # return remain[0]/moved[0] if moved[0]!=0 else 0