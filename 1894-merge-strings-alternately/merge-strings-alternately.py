class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        lst=[]
        while i<len(word1) or j<len(word2):
            if i<len(word1):
                lst.append(word1[i])
                i+=1
            if j<len(word2):
                lst.append(word2[j])
                j+=1
        return "".join(lst)