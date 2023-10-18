class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = {i: [] for i in range(n)}
        indegrees = [0] * n
        for u, v in relations:
            graph[u-1].append(v-1)
            indegrees[v-1] += 1
        
        # BFS
        queue = []
        for i in range(n):
            if indegrees[i] == 0:
                queue.append(i)

        max_time = time.copy()

        while queue:
            curr = queue.pop(0)
            for neighbor in graph[curr]:
                max_time[neighbor] = max(max_time[neighbor], max_time[curr] + time[neighbor])
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return max(max_time)