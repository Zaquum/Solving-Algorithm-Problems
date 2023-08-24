class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0

        for word in words:
            if num_of_letters + len(word) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [word]
            num_of_letters += len(word)

        # Handle the last line separately
        last_line = ' '.join(cur)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)

        return res