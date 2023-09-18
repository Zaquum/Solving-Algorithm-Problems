class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        pairs = []
        for i, char in enumerate(s):
            if char in vowels:
                pairs.append(i)
        n = len(pairs)
        s_list = list(s)
        for i in range(n//2):
            tmp = s_list[pairs[i]]
            s_list[pairs[i]] = s_list[pairs[n - i - 1]]
            s_list[pairs[n - i - 1]] = tmp
        return ''.join(s_list)