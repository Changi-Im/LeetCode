class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        hmap = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", \
                90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        val = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        i = len(val) - 1
        ret = ""
        while num > 0:
            j = 0
            while num - val[i] >= 0:
                j += 1
                num -= val[i]
                ret += hmap[val[i]]
            i -= 1 
        
        return ret