class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # No books means no height

        for i in range(1, n + 1):
            current_thickness = 0
            max_height_in_shelf = 0
            # Try to place books[i-1] on a new shelf or extend the current shelf
            for j in range(i, 0, -1):
                current_thickness += books[j-1][0]
                if current_thickness > shelfWidth:
                    break
                max_height_in_shelf = max(max_height_in_shelf, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1] + max_height_in_shelf)

        return dp[n]