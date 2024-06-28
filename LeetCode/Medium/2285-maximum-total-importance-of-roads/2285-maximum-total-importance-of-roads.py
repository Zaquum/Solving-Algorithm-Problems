class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Code from GPT
        
        # Step 1: Count the degree of each city
        degree = defaultdict(int)
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1

        # Step 2: Sort cities by degree in descending order
        sorted_cities = sorted(degree.keys(), key=lambda x: degree[x], reverse=True)

        # Step 3: Assign values to cities from n to 1
        values = [0] * n
        current_value = n
        for city in sorted_cities:
            values[city] = current_value
            current_value -= 1

        # Step 4: Calculate the total importance of all roads
        total_importance = 0
        for a, b in roads:
            total_importance += values[a] + values[b]

        return total_importance