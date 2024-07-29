class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # From GPT
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Use a priority queue to perform a modified BFS
        pq = [(0, 1, 0)]  # (current time, current node, path count)
        first_min_time = [float('inf')] * (n + 1)
        second_min_time = [float('inf')] * (n + 1)
        first_min_time[1] = 0

        while pq:
            cur_time, node, count = heapq.heappop(pq)

            for neighbor in graph[node]:
                # Calculate the new time to reach the neighbor
                wait_time = 0
                cycle = cur_time // change
                if cycle % 2 == 1:  # If it's red light period
                    wait_time = change - (cur_time % change)

                new_time = cur_time + wait_time + time

                # Update first or second minimum times accordingly
                if new_time < first_min_time[neighbor]:
                    first_min_time[neighbor], new_time = new_time, first_min_time[neighbor]
                    heapq.heappush(pq, (first_min_time[neighbor], neighbor, count))
                if first_min_time[neighbor] < new_time < second_min_time[neighbor]:
                    second_min_time[neighbor] = new_time
                    heapq.heappush(pq, (second_min_time[neighbor], neighbor, count + 1))

        return second_min_time[n] if second_min_time[n] != float('inf') else -1