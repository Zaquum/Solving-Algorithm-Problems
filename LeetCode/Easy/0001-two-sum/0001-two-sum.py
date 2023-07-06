class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a, b in itertools.combinations(enumerate(nums),2):
            if a[1]+b[1] == target:
                return [a[0],b[0]]