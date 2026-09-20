class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        sp = 0
        ep = len(numbers) - 1

        while ep > sp:
            l = numbers[sp]
            r = numbers[ep]

            if l + r == target: 
                return [sp + 1, ep + 1]

            if l + r > target:
                ep -= 1
            else:
                sp += 1