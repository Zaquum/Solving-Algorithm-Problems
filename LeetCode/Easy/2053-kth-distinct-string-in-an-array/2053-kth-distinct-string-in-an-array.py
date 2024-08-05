class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = defaultdict(int)
        for s in arr:
            counts[s] += 1
        ans = ""
        cur_cnt = 0
        for s in arr:
            if counts[s] == 1:
                cur_cnt += 1
                if cur_cnt == k:
                    ans = s
                    break
        return ans
                    