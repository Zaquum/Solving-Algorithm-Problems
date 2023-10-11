class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted([flower[0] for flower in flowers])
        ends = sorted([flower[1] for flower in flowers])


        def binary_search(array, x):
            low, high = 0, len(array) - 1
            while low <= high:
                mid = (low + high) // 2
                if array[mid] <= x:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        ans = []
        for person in people:
            started = binary_search(starts, person)
            ended = binary_search(ends, person - 1)
            ans.append(started - ended)
    
        return ans