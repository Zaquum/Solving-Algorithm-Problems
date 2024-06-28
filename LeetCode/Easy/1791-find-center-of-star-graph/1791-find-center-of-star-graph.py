class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        cnts = defaultdict(int)
        for start, end in edges:
            cnts[start] += 1
            cnts[end] += 1
            if cnts[start] > 1:
                return start
            if cnts[end] > 1:
                return end