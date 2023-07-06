class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # need to solve later

        q = []  # maxHeap: (max possible day, r, c)
        grid = [[0 for _ in range(col)] for _  in range(row)]
        # create the grid with max possible day per cell
        for i, (r, c) in enumerate(cells):
            grid[r - 1][c - 1] = (i + 1)
        visited = set()

        # add the top row to the maxHeap queue
        for c in range(col):
            q.append((-grid[0][c], 0, c))
        heapq.heapify(q)

        while q:
            day, r, c = heapq.heappop(q)
            # if we've reached the bottom, return the max day immediately
            if r == (row - 1): 
                return -(day + 1)
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newR, newC = r + x, c + y
                if newR < 0 or newR >= row or newC < 0 or newC >= col or (newR, newC) in visited:
                    continue
                # using max() function, but it's technically taking the 'min'
                # this is because of Python's maxHeap implementation
                d = max(day, -grid[newR][newC])
                heapq.heappush(q, (d, newR, newC))
                visited.add((newR, newC))
