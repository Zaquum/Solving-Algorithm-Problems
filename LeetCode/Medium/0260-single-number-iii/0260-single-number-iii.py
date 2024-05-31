class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
            
        rightmost = xor & -xor
        # print(rightmost)
        result = [0, 0]
        # 3 5 -> 011 101 -> 010
        for num in nums:
            if num & rightmost:
                print(num)
                result[0] ^= num
            else:
                result[1] ^= num
        return result