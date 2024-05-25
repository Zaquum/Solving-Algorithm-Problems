class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ans = []
        
        def dfs(pre_idx, idx, cur_path):
            # Return
            if idx == len(s):
                if s[pre_idx:idx] in wordDict:
                    self.ans.append(cur_path + s[pre_idx:idx])
                return
            
            # Include the current substring if it's in wordDict
            if s[pre_idx:idx] in wordDict:
                dfs(idx, idx, cur_path + s[pre_idx:idx] + " ")
            
            # Move to the next index (exclude)
            dfs(pre_idx, idx + 1, cur_path)
        
        dfs(0, 0, "")
        return self.ans