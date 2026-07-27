class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
        for count in freq.values():
            if count>=2:
                return True
        
        return False
