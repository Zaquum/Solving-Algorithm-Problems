class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(square):
            s = 15
            return (sum(square[0]) == s and
                    sum(square[1]) == s and
                    sum(square[2]) == s and
                    sum([square[i][0] for i in range(3)]) == s and
                    sum([square[i][1] for i in range(3)]) == s and
                    sum([square[i][2] for i in range(3)]) == s and
                    sum([square[i][i] for i in range(3)]) == s and
                    sum([square[i][2 - i] for i in range(3)]) == s)

        def is1to9(square):
            nums = [square[i][j] for i in range(3) for j in range(3)]
            return sorted(nums) == list(range(1, 10))

        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows - 2):
            for c in range(cols - 2):
                subgrid = [grid[r + i][c + j] for i in range(3) for j in range(3)]
                square = [subgrid[:3], subgrid[3:6], subgrid[6:]]
                if is1to9(square) and isMagic(square):
                    count += 1

        return count