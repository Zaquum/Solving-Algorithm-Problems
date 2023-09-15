class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1]-p2[1])

        n = len(points)
        c = collections.defaultdict(list)
        visited = [False] * n
        
        for i in range(n):
            for j in range(i+1, n):
                d = distance(points[i], points[j])
                c[i].append((d,j))
                c[j].append((d,i))
        cnt = 1
        ans = 0
        visited[0] = 1
        heap = c[0]
        heapq.heapify(heap)
        while heap:
            d,j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt+1, ans+d
                for dis in c[j]:
                    heapq.heappush(heap, dis)
            if cnt == n:
                break
        return ans