class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        
        for i, n in enumerate(nums):
            complement = target - n
            if hmap.get(complement) is not None:
                return [hmap[complement], i]
            
            hmap[n] = i
        
        return False
                    
