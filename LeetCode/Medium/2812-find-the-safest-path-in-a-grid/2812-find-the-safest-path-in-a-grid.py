from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # Did not solve
        # Below is someone's solution
        
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return 0
        
        # Get location of all thefts
        ones = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    ones.add((i, j))
        
        # Compute the Manhattan distance to the closest theft of each grid
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        distance = [[float('inf')] * n for _ in range(n)]
        for x, y in ones:
            q = deque([(x, y, 0)])
            seen = set()
            while q:
                row, col, d = q.popleft()
                if (row, col) in seen:
                    continue
                seen.add((row, col))

                # Pruning here. Can be pretty slow if add all possible grid to the heap
                if d >= distance[row][col]:
                    continue
                distance[row][col] = d
                for direction in directions:
                    newRow, newCol = row + direction[0], col + direction[1]
                    if 0 <= newRow < n and 0 <= newCol < n:
                        q.append((newRow, newCol, d + 1))

        # Greedy search for the next grid of max distance until reach the end
        h = [(-distance[0][0], 0, 0)]
        visited = set([(0, 0)])
        res = float('inf')
        while h:
            d, row, col = heapq.heappop(h)
            # safeness factor is determined by the smallest distance
            res = min(res, -d)
            if row == n - 1 and col == n - 1:
                return res
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                if 0 <= newRow < n and 0 <= newCol < n:
                    if (newRow, newCol) in visited:
                        continue
                    heapq.heappush(h, (-distance[newRow][newCol], newRow, newCol))
                    visited.add((newRow, newCol))