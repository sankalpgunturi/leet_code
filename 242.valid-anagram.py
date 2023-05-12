class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}

        for x in range(len(s)):
            s_dict[s[x]] = 1 + s_dict.get(s[x], 0)
            t_dict[t[x]] = 1 + t_dict.get(t[x], 0)

        for x in s_dict:
            if s_dict[x] != t_dict.get(x, 0):
                return False
        
        return True
        
