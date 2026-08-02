class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()  # [0, 1, 3, 5, 6]
        max_h = 0
        h = 0
        n = len(citations)
        for i in range(len(citations)):
            c = citations[i]  
            if c > max_h:
                max_h = c # 1
                if max_h <= n - i:
                    h = max_h
                else:
                    if h <= n - i:
                        h = n - i

        return h
                
            
            
            

        