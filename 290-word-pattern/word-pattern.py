
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        p_to_w = {}
        w_to_p = {}
        
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]
            
            if p in p_to_w and p_to_w[p] != w:
                return False
            
            if w in w_to_p and w_to_p[w] != p:
                return False
            
            p_to_w[p] = w
            w_to_p[w] = p
        
        return True
        