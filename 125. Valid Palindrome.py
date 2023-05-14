class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def modify(string):
            string = string.lower().replace(" ", "")
            i = 0
            while i < len(string):
                n = string[i]
                if not n.isalnum():
                    string = string[:i] + string[(i+1):]
                    i -= 1
                i += 1

            return string

        t, s_modified, t_modified = "", "", ""
        t = s[::-1]

        s_modified = modify(s)
        t_modified = modify(t)

        if s_modified == t_modified:
            return True
        else:
            return False
            
