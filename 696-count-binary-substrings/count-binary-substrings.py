class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        prev_group = 0
        curr_group = 1
        count = 0
        
        for i in range(1, len(s)):
            
            if s[i] == s[i-1]:
                curr_group += 1
            else:
                count += min(prev_group, curr_group)
                prev_group = curr_group
                curr_group = 1
        
        count += min(prev_group, curr_group)
        
        return count
