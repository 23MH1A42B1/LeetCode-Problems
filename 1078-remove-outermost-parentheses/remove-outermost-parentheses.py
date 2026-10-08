class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        count=0
        for c in s:
            if c =='(':
                count+=1
                if count>1:
                    stack.append(c)
            else:
                count-=1
                if count>0:
                    stack.append(c)
        return "".join(stack)