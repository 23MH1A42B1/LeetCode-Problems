from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r1=Counter(ransomNote)
        m1=Counter(magazine)
        return r1<=m1