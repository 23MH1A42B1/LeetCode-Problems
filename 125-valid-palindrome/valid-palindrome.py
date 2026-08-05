class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst1=[]
        for st in s:
            if st.isalnum():
                lst1.append(st.lower())
        left,right=0,len(lst1)-1
        while left<right:
            if lst1[left]!=lst1[right]:
                return False
            left+=1
            right-=1
        return True
