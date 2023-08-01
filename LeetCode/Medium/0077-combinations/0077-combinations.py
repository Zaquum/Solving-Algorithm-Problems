class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def solve(path, ans, i ,k):
            if k == 0:
                ans.append(list(path)) # copy list
                return
            for idx in range(i, n+1):
                path.append(idx)
                solve(path, ans, idx+1, k-1)
                path.remove(idx)
        
        solve(path, ans, 1, k)
        return ans