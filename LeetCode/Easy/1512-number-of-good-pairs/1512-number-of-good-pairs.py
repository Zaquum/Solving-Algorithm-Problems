class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def factorial(n : int) -> int:
            if n == 1 or n == 0:
                return 1
            return n * factorial(n-1)
        def combination(a: int, b: int) -> int: #aCb
            return factorial(a)/(factorial(b)*factorial(a-b))
        count = {}
        ans = 0
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, cnt in count.items():
            if cnt >= 2:
                ans += combination(cnt, 2)
        # for num, cnt in count.items():
        #     if cnt >= 2:
        #         ans += cnt * (cnt - 1) // 2
        return int(ans)