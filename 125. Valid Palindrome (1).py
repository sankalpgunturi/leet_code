class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_string = ""

        for char in s:
            if char.isalnum():
                new_string += char.lower()
        
        return new_string == new_string[::-1]
        
