class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dt={}
        for i in range(len(nums)):
            if nums[i] in dt and abs(dt[nums[i]]-i)<=k:
                return True
            else:
                dt[nums[i]]=i
        return False
                
            