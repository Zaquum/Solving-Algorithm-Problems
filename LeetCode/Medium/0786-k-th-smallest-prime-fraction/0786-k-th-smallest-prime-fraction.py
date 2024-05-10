class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        arrs = []
        for arr in itertools.permutations(arr, 2):
            arrs.append(arr)
        arrs.sort(key = lambda x:x[0]/x[1])
        return arrs[k-1]