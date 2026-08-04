class Solution:
    def countSeniors(self, details: List[str]) -> int:
        lst=[]
        for age in details:
            lst.append(age[11:13])
        count=0
        for i in range(len(lst)):
            if lst[i]>"60":
                count+=1
        return count
