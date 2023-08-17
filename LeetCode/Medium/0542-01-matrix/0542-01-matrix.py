class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[0] * n for _ in range(m)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        q = collections.deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = m*n
        
        while q:
            y, x = q.popleft()
            for dy, dx in directions:
                ny = y + dy
                nx = x + dx
                if 0<=ny<m and 0<=nx<n and mat[ny][nx] > mat[y][x] + 1:
                    mat[ny][nx] = mat[y][x] + 1
                    q.append((ny,nx))

        return mat