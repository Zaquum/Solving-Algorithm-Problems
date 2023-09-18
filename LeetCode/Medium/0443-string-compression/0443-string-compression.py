class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        i = 0
        while i < len(chars):
            char = chars[i] # cur
            count = 1
            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                i += 1
                count += 1
            chars[index] = char
            index += 1
            if count > 1:
                for c in str(count):
                    chars[index] = c
                    index += 1
            i += 1
        # chars = chars[:index]
        return index