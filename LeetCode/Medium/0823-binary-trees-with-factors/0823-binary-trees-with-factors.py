class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        n = len(arr)
        dp = {x: 1 for x in arr}

        for i in range(n):
            for j in range(i+1):
                if arr[i] * arr[j] in dp:
                    if i != j:
                        dp[arr[i] * arr[j]] += (dp[arr[i]] * dp[arr[j]]*2) % MOD
                    elif i == j:
                        dp[arr[i] * arr[j]] += (dp[arr[i]] * dp[arr[j]]) % MOD    
                        # print(i, j)
                
        return sum(dp.values()) % MOD
