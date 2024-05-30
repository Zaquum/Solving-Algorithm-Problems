class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        n = len(arr)

        # Calculate prefix XOR sums
        prefix_xor = [0] * (n + 1)
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        # Iterate through prefix XOR sums to find sub-arrays with XOR equal to 0
        for i in range(n):
            for k in range(i + 1, n):
                if prefix_xor[i] == prefix_xor[k+1]:
                    count += k - i

        return count