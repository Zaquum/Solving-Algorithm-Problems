# from sortedcontainers import SortedList

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # sortedNums = SortedList(list(map(lambda num: num if num%2 == 0 else 2*num, nums)))
        # ans = int(1e9)
        # while sortedNums[-1] % 2 == 0:
        #     tmp = int(sortedNums[-1]/2)
        #     sortedNums.pop(-1)
        #     sortedNums.add(tmp)
        #     ans = min(ans, sortedNums[-1] - sortedNums[0])
        # return ans

        minHeap, heapMax = [],0
        for n in nums:
            tmp = n
            while n%2==0:
                n = n//2
            minHeap.append((n, max(tmp, 2*n)))
            heapMax = max(heapMax, n)

            # 1 -> 2
            # 2 -> 1
            # 4 -> 2 -> 1

        res = float("inf")
        heapq.heapify(minHeap)
        while len(minHeap) == len(nums):
            n, nMax = heapq.heappop(minHeap) # minHeap is pairs of (n, tmp)
            res = min(res, heapMax - n)

            if n < nMax:
                heapq.heappush(minHeap, (n*2,nMax)) 
                heapMax = max(heapMax, n*2)
        return res