class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left=0
        right=len(s)-1
        char=list(s)
        while left<right:
            if not char[left].isalpha():
                left+=1
            elif not char[right].isalpha():
                right-=1
            else:
                char[left],char[right]=char[right],char[left]
                left+=1
                right-=1
        return "".join(char)