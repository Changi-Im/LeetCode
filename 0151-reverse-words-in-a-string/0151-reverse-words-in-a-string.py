class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        prev = ""
        cur = ""
        ret_list = []
        
        for ss in s:
            if ss == " ":
                if cur != "":
                    prev = cur
                    ret_list.append(prev)
                cur = ""
            else:
                cur += ss
        
        if cur != "":
            ret_list.append(cur)

        ret = ""
        for i in range(len(ret_list) - 1, -1, -1):
            ret += ret_list[i]
            ret += " "
        
        return ret[:-1]