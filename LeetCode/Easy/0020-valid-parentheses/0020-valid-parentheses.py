class Solution:
    def isValid(self, s: str) -> bool:
        s_list=list(s)
        
        stack=[]
        answer = True
        for i in s_list:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            elif len(stack)!=0:
                if (i==']' and stack[-1]=='[') or (i==')' and stack[-1]=='(') or (i=='}' and stack[-1]=='{'):
                    stack.pop()
                else:
                    answer = False
                    break
            else:
                answer = False
                break
                
        if len(stack)!=0:
            answer = False
        return answer