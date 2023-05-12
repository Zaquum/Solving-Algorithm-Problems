class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @lru_cache(None)
        def dfs(idx):
            if idx >= n:
                return 0
            return max(dfs(idx+1),questions[idx][0] + dfs(idx+questions[idx][1]+1))
        return dfs(0)