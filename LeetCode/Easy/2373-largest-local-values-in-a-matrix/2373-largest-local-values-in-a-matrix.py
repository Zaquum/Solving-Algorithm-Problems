class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * (n-2) for _ in range(n-2)]
        for i in range(1, n-1):
            for j in range(1, n-1):
                tmp = grid[i][j]
                for k in range(-1,2):
                    for l in range(-1,2):
                        tmp = max(tmp, grid[i+k][j+l])
                ans[i-1][j-1] = tmp
        return ans