class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = [("a","b","c"),("d","e","f"),("g","h","i"),("j","k","l"),("m","n","o"),("p","q","r","s"),("t","u","v"),("w","x","y","z")]
        n = len(digits)
        ans = []
        def solve(idx, combi):
            if idx == n:
                ans.append(combi)
                return
            letters_idx = int(digits[idx])-2
            for letter in letters[letters_idx]:
                solve(idx+1, combi+letter)

        solve(0, "")
        return ans