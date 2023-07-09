class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        
        def outside(x, y):
            if x < 0 or x >= row or y < 0 or y >= col:
                return True
            return False
        
        visited = [[False] * col for _ in range(row)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        x = 0
        y = 0
        
        ans = [matrix[0][0]]
        visited[0][0] = True
        
        idx = 0
        size = 1
        while (True):
            if (size == row * col):
                break
            
            dx = directions[idx%4][0]
            dy = directions[idx%4][1]
            
            if (outside(x+dx, y+dy)):
                idx += 1
                continue
            if (visited[x+dx][y+dy]):
                idx += 1
                continue
            x = x + dx
            y = y + dy
            ans.append(matrix[x][y])
            visited[x][y] = True
            size += 1
            
        return ans