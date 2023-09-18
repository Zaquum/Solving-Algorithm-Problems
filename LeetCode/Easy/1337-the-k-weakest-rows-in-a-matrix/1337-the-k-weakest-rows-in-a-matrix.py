class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        min_heap = []
        for i, row in enumerate(mat):
            soldiers = sum(row)
            heappush(min_heap, (soldiers, i))

        result = []
        for _ in range(k):
            result.append(heappop(min_heap)[1])
        
        return result