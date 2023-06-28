class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # get direct graph
        graph = {}
        for i in range(len(edges)):
            cur_edge = edges[i]
            cur_prob = succProb[i]
            graph.setdefault(cur_edge[0], []).append((cur_edge[1], cur_prob))
            graph.setdefault(cur_edge[1], []).append((cur_edge[0], cur_prob))
        
        visited = set()

        max_heap = [(-1,start)]

        while max_heap:
            prob, cur = heappop(max_heap)
            visited.add(cur)
            if cur == end:
                return -prob
            for neigh, p in graph.get(cur, []):
                if not neigh in visited:
                    new_prob = -1 * abs(prob * p)
                    heappush(max_heap, (new_prob, neigh))

        return 0