class Solution:
    def largestVariance(self, s: str) -> int:
        # O(n^2) - fail
        # solve later

        # O(2 * n)
        def solve(a,b):
            max_var = 0
            var = 0
            has_b = False
            first_b = False
            
            for c in s:
                if c == a:
                    var +=1
                elif c == b:
                    has_b = True

                    if first_b and var >= 0:
                        first_b = False
                    elif(var-1) < 0:
                        first_b = True
                        var = -1
                    else:
                        var -= 1
                if has_b and var > max_var:
                    max_var = var
            return max_var

        max_var = 0
        for a in set(s):
            for b in set(s):
                if a == b :
                    continue
                var = solve(a,b)
                max_var = max(max_var, var)

        return max_var

        
        # below is O(26^2 * n) = O(n)
        
        # def kadane(a:str, b:str) -> int:
        #     ans = 0
        #     cnt_a, cnt_b = 0, 0
        #     canExtend = False
            
        #     for c in s:
        #         if c != a and c != b:
        #             continue
        #         if c == a:
        #             cnt_a += 1
        #         elif c == b:
        #             cnt_b += 1
        #         if cnt_b > 0:
        #             ans = max(ans, cnt_a - cnt_b)
        #         elif cnt_b == 0 and canExtend:
        #             ans = max(ans, cnt_a - 1)

        #         if cnt_b > cnt_a:
        #             cnt_a = 0
        #             cnt_b =0
        #             canExtend = True
        #     return ans

        # return max(kadane(c1, c2)
        # for c1 in string.ascii_lowercase
        # for c2 in string.ascii_lowercase
        # if c1 != c2)