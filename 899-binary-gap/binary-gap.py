class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:] 
        
        last = -1
        max_gap = 0
        
        for i in range(len(binary)):
            if binary[i] == '1':
                if last != -1:
                    max_gap = max(max_gap, i - last)
                last = i
        
        return max_gap