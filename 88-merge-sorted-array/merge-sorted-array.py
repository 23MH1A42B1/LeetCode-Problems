class Solution:
    def merge(self, nums1, m, nums2, n):
        lst = []

        for i in range(m):
            lst.append(nums1[i])

        for i in range(n):
            lst.append(nums2[i])

        lst.sort()

        for i in range(len(lst)):
            nums1[i] = lst[i]