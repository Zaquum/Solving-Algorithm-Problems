class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:  # length 1 is return it
            return len(chars)
        i = 0 # idx of chars
        j = 0 # idx of s
        while i < len(chars):
            cnt = 1
            while i < len(chars)-1 and chars[i] == chars[i+1]: # increase through a same word
                cnt += 1
                i += 1
            
            chars[j] = chars[i] # append to s
            j += 1
            if cnt > 1 :
                for val in str(cnt): # update the lenght of the word
                    chars[j] = val
                    j += 1
            
            i += 1

        return j