class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        from collections import defaultdict
        let_dic = defaultdict(int)
        for letter in letters:
            let_dic[letter] += 1
        
        def dfs(idx, dic):
            if idx == len(words):
                total_score = 0
                for key, count in dic.items():
                    if count > 0: 
                        let_idx = ord(key) - ord('a')
                        total_score += score[let_idx] * count
                return total_score
            
            exclude = dfs(idx + 1, dic.copy())
            
            can_include = True
            temp_dic = dic.copy()
            for ch in words[idx]:
                temp_dic[ch] += 1
                if temp_dic[ch] > let_dic[ch]:
                    can_include = False
                    break
            
            include = dfs(idx + 1, temp_dic) if can_include else 0
            
            return max(exclude, include)
        
        return dfs(0, defaultdict(int))