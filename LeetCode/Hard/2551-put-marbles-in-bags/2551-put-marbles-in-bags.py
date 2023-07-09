class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if n == k:
            return 0
        bag = [0] * (n-1)
        for i in range(n-1):
            bag[i] = weights[i] + weights[i+1]
        bag.sort()

        max_fair = sum(bag[n-k:])
        min_fair = sum(bag[:k-1])

        print(min_fair)
        print(max_fair)
        return max_fair - min_fair