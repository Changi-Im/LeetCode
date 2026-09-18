class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        i = len(s) - 1
        
        ret = 0
        prev = -1
        while i >= 0:
            cur = s[i]
            if (cur == "I" and (prev == "V" or prev == "X")) \
            or (cur == "X" and (prev == "L" or prev == "C")) \
            or (cur == "C" and (prev == "D" or prev == "M")):
                ret -= hmap[cur]
            else:
                ret += hmap[cur]
            
            prev = cur
            i -= 1

        return ret