class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest_word = ""
        shortest_len = 1 << 8

        for s in strs:
            if len(s) < shortest_len:
                shortest_len = len(s)
                shortest_word = s

        for s in strs:
            for i in range(len(shortest_word)):
                if s[i] != shortest_word[i]:
                    shortest_word = s[:i]
                    break
            if shortest_word == "":
                return ""
        
        return shortest_word
