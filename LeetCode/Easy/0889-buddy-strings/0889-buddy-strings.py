class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal and len(s) != len(set(s)):
            return True
        
        swap_num = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                swap_num.append(i)
                if len(swap_num) > 2 :
                    return False
        return len(swap_num) == 2 and s[swap_num[0]] == goal[swap_num[1]] and s[swap_num[1]] == goal[swap_num[0]]