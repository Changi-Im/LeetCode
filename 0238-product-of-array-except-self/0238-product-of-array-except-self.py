class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # [1,2,3,4]
        # prefix: [1, 1, 1*2, 1*2*3]
        # suffix: [1, 4, 4*3, 4*3*2]
        # ans: [4*3*2, 1 * 4*3, 1*2 * 4 1*2*3]

        # create prefix and suffix array
        prefix, suffix = [1], [1]
        n = len(nums)

        for i in range(1, n):
            prefix.append(prefix[i - 1] * nums[i - 1])
            suffix.append(suffix[i - 1] * nums[n - i])

        # create answer array
        ans = []
        for i in range(n):
            ans.append(prefix[i]*suffix[n - i - 1])

        return ans

