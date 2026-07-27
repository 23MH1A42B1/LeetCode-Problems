class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst1 = []

        for ch in s:
            if ch.isalnum():
                lst1.append(ch.lower())

        left = 0
        right = len(lst1) - 1

        while left < right:
            if lst1[left] != lst1[right]:
                return False

            left += 1
            right -= 1

        return True