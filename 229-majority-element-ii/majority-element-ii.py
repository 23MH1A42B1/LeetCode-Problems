class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        ans = []

        for numb in freq:
            if freq[numb]>len(nums)/3:
                ans.append(numb)

        return ans