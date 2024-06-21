class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        total_satisfied = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        
        extra_satisfied = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        
        max_extra_satisfied = extra_satisfied
        for i in range(minutes, n):
            if grumpy[i] == 1:
                extra_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                extra_satisfied -= customers[i - minutes]
            max_extra_satisfied = max(max_extra_satisfied, extra_satisfied)
        
        return total_satisfied + max_extra_satisfied                    