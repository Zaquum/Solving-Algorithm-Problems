class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_number(num):
            mapped = ''.join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped)

        mapped_nums = [(num, map_number(num)) for num in nums]

        mapped_nums.sort(key=lambda x: x[1])

        sorted_nums = [num for num, mapped in mapped_nums]

        return sorted_nums