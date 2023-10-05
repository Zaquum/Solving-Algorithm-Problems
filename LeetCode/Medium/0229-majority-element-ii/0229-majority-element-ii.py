class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = (len(nums))//3
        ans = []
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num,0) + 1
            if cnt[num] > threshold:
                ans.append(num)
        return set(ans)