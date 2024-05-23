class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def dfs(idx, elems):
            if idx == len(nums):
                if elems:
                    return 1
                else:
                    return 0
                
            tmp = 0
            flag = False
            for elem in elems:
                if abs(elem - nums[idx]) == k:
                    flag = True
                    break

            if not flag:
                tmp += dfs(idx + 1, elems + [nums[idx]])
                
            # Always option to not include the current number
            tmp += dfs(idx + 1, elems)

            return tmp

        return dfs(0, [])