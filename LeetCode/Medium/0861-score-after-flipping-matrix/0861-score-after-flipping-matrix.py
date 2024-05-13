class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Step 1: Optimize Rows
        for i in range(rows):
            if grid[i][0] == 0:
                for j in range(cols):
                    grid[i][j] ^= 1

        # Step 2: Optimize Columns
        for j in range(1, cols):
            count = sum(grid[i][j] for i in range(rows))
            if count < (rows + 1) / 2:
                for i in range(rows):
                    grid[i][j] ^= 1

        # Step 3: Calculate Score
        score = 0
        for row in grid:
            score += int(''.join(map(str, row)), 2)

        return score