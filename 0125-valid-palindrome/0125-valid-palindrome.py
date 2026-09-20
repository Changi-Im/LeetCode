class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sp = 0
        ep = len(s) - 1

        def is_alphanumeric(ch): 
            return (ch >= "a" and ch <= "z") or (ch >= "0" and ch <= "9")

        while ep > sp:
            r = s[ep].lower()
            l = s[sp].lower()
            
            if not is_alphanumeric(r) and not is_alphanumeric(l):
                ep -= 1
                sp += 1
                continue
            elif not is_alphanumeric(r):
                ep -= 1
                continue
            elif not is_alphanumeric(l):
                sp += 1
                continue
            if r != l:
                return False
            ep -= 1
            sp += 1
        return True