class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnts = defaultdict(int)
        for elem in arr1:
            cnts[elem] += 1
        front = []
        end = []
        for i, elem in enumerate(arr2):
            front += [arr2[i]] * cnts[arr2[i]]
            del cnts[arr2[i]]
        for elem, cnt in cnts.items():
            end += [elem] * cnt
        end.sort()
        return front + end