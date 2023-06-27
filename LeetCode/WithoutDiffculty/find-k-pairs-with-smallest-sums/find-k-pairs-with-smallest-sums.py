class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = [[nums1[0], nums2[0]]]
        hq = []
        idx1, idx2 = 0, 0
        cnt = 1
        addedset = set()
        while cnt < k:
            if idx1 + 1 < len(nums1):
                tmp = (nums1[idx1+1]+nums2[idx2], idx1+1, idx2)
                if tmp not in addedset:
                    heapq.heappush(hq, tmp)
                    addedset.add(tmp)
            
            if idx2 + 1 < len(nums2):
                tmp = (nums1[idx1]+nums2[idx2+1], idx1, idx2+1)
                if tmp not in addedset:
                    heapq.heappush(hq, tmp)
                    addedset.add(tmp)
            # end of idx
            if len(hq) == 0:
                break

            _, idx1, idx2 = heapq.heappop(hq)

            ans.append([nums1[idx1], nums2[idx2]])
            cnt += 1

        return ans