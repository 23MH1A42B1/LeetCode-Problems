class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        if n == 1:
            return "0"
        
        mid = 2 ** (n - 1)
        
        if k == mid:
            return "1"
        
        if k < mid:
            return self.findKthBit(n - 1, k)
        
        mirror = 2 ** n - k
        bit = self.findKthBit(n - 1, mirror)
        
        return "1" if bit == "0" else "0"