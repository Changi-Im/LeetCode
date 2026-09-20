class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        sp = 0
        
        for tp in range(len(t)):
            if t[tp] == s[sp]:
                sp += 1
            if sp > len(s) - 1:
                return True

        return False
