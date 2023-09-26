class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # bcabc -> abc
        # cbacdcbc -> acdb
        dic = {}
        stack = []
        selected = set()

        for c in s:
            dic[c] = dic.get(c,0) + 1

        for c in s:
            # dic[c] -= 1
            if c not in selected:
                while stack and dic[stack[-1]] > 0 and stack[-1] > c:
                    selected.remove(stack.pop())
                stack.append(c)
                selected.add(c)
            dic[c] -= 1
        return "".join(stack)