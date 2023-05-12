class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        x = 0
        while s and t:
            if t[x] not in s:
                return False
            else:
                s = s.replace(t[x], "", 1)
                t = t[:x] + t[(x+1):]
        
        if len(t) == 0:
            return True
        else:
            return False
          
