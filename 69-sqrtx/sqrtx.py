class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        left,right=0,x//2
        ans=0
        while left<=right:
            mid=(left+right)//2
            num=mid*mid
            if num==x:
                return mid
            elif num<x:
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans
