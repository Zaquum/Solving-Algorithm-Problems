class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        ans = float('-inf')
        sets = set()
        for num in nums:
            if -num in sets:
                ans = max(ans, abs(num))
            else:
                sets.add(num)
        # print("End Testcase")
        return ans if ans != float('-inf') else -1
        