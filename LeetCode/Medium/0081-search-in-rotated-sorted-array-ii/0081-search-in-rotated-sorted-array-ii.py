class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start+end)//2
            print(mid)
            if nums[mid] == target:
                return True
            # fail to find sorted array
            if nums[mid] == nums[end]: 
                end -= 1
                continue
            # left sorted
            if nums[start] <= nums[mid]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # right sorted
            else:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False
