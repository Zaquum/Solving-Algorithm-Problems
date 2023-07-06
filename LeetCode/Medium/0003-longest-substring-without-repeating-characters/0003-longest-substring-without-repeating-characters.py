class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str_list=[]
        ret=0
        for cursor in range(len(s)):
            count_dict={s[cursor]:1}
            for move in range(cursor+1,len(s)):
                if count_dict.get(s[move],False):
                    sub_str_list.append(''.join(count_dict.keys()))
                    break
                else:
                    count_dict[s[move]]=1
            sub_str_list.append(''.join(count_dict.keys()))
        
        if len(sub_str_list) !=0:
            ret = len(max(sub_str_list,key=lambda x: len(x)))
            
        return ret