class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_ = ""

        for i in range(len(s)):
            ss = s[i].lower()
            if (ss >= "a" and ss <= "z") \
                or (ss >= "0" and ss <= "9"):
                s_ += ss

        sp = 0
        ep = len(s_) - 1
        while ep > sp:
            if s_[sp] != s_[ep]:
                return False
            sp += 1
            ep -= 1
        
        return True