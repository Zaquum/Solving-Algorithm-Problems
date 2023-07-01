class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # best = 0
        def dfs(i:int):
            # non local 선언
            nonlocal unfairness


            if i == len(cookies):
                unfairness = min(unfairness, max(split))
                return
            # ready - split to kid
            if len(split) < k:
                split.append(cookies[i])
                dfs(i+1)
                split.pop()
            # distributed = set()
            for j in range(len(split)):
                # if split[j] + cookies[i] < unfairness and split[j] not in distributed :
                #     distributed.add(split[j])
                split[j] += cookies[i]
                dfs(i+1)
                split[j] -= cookies[i]

        split = []
        unfairness = float("inf")
        dfs(0)
        return unfairness