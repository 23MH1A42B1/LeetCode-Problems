class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1={}
        s2={}
        for st in s:
            if st not in s1:
                s1[st]=1
            else:
                s1[st]+=1
        for ts in t:
            if ts not in s2:
                s2[ts]=1
            else:
                s2[ts]+=1
        return s1==s2