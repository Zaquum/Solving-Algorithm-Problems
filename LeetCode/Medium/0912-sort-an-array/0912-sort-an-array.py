class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            left, right = arr[l:m+1] , arr[m+1:r+1]
            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, left, right):
            if left == right:
                return arr
            
            mid = (left + right)//2
            mergeSort(arr, left, mid)
            mergeSort(arr, mid+1, right)
            merge(arr, left, mid, right)
            return arr

        return mergeSort(nums, 0, len(nums)-1)