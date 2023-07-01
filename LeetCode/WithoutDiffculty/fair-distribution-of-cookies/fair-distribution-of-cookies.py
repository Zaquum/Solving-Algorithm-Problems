class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # best = 0
        child = [0] * k
        unfairness = float("inf")

        def dfs(i:int):
            # non local 선언
            nonlocal unfairness
            
            if i == len(cookies):
                unfairness = min(unfairness, max(child))
                return
            # already optimal solution
            if unfairness <= max(child): 
                return

            for j in range(k):
                child[j] += cookies[i]
                dfs(i+1)
                child[j] -= cookies[i]

        dfs(0)
        return unfairness