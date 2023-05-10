class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]
        col_idx = 0
        row_idx = 0
        direct = [(0,1),(1,0),(0,-1),(-1,0)]
        dir_idx = 0
        num = 1
        mat[0][0] = num
        while True:
            if num == n*n:
                break
            
            dx = direct[dir_idx%4][0]
            dy = direct[dir_idx%4][1]
            row_idx += dx
            col_idx += dy

            if row_idx < 0 or row_idx >= n or col_idx <0 or col_idx >= n:
                dir_idx += 1
                row_idx -= dx
                col_idx -= dy
                continue
            if mat[row_idx][col_idx] != 0:
                dir_idx += 1
                row_idx -= dx
                col_idx -= dy
                continue
            num += 1
            mat[row_idx][col_idx] = num
        return mat