from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=Counter(s)
        t1=Counter(t)
        return s1==t1