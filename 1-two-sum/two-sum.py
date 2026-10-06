class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen={}
        for i in range(len(nums)):
            num=nums[i]
            need=target-num
            if need in seen:
                return [seen[need],i] 
            seen[num]=i
        