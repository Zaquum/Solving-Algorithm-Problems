class Solution:
    def minDeletions(self, s: str) -> int:
        dict_s = {}
        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1
        
        sorted_s = sorted(dict_s.items(), key=lambda x: x[1])

        cnt_set = set()
        prev_cnt = 0
        ans = 0
        for char, cnt in sorted_s:
            if cnt in cnt_set:
                sub_cnt = 0
                while cnt in cnt_set:
                    cnt -= 1
                    sub_cnt += 1
                    if cnt <=0:
                        break
                ans += sub_cnt
                cnt_set.add(cnt)
            else:
                cnt_set.add(cnt)
        return ans 
