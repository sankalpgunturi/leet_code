class Solution:
    def isPalindrome(self, s: str) -> bool:
        final = True
        l = 0
        r = len(s) - 1

        s = s.lower()
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while r > 0 and not s[r].isalnum():
                r -= 1

            if l < r and not s[l] == s[r]:
                final = False
                return final

            l += 1
            r -= 1

        return final
