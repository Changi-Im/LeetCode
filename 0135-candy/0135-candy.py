class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 1:
            return 1

        candies = []
        for _ in range(n):
            candies.append(1)

        for i in range(n):
            if i + 1 >= n: # last index
                if ratings[i] > ratings[i-1]:
                    candies[i] = candies[i-1] + 1
            elif i - 1 < 0: # first index
                if ratings[i] > ratings[i+1]:
                    candies[i] = candies[i+1] + 1
            else: # in general
                if ratings[i] > ratings[i-1]:
                    if candies[i] <= candies[i-1]:
                        candies[i] = candies[i-1] + 1
                
                if ratings[i] > ratings[i+1]:
                    if candies[i] <= candies[i+1]:
                        candies[i] = candies[i+1] + 1

        for i in range(n-1, -1, -1):
            if i + 1 >= n: # last index
                if ratings[i] > ratings[i-1]:
                    candies[i] = candies[i-1] + 1
            elif i - 1 < 0: # first index
                if ratings[i] > ratings[i+1]:
                    candies[i] = candies[i+1] + 1
            else: # in general
                if ratings[i] > ratings[i-1]:
                    if candies[i] <= candies[i-1]:
                        candies[i] = candies[i-1] + 1
                
                if ratings[i] > ratings[i+1]:
                    if candies[i] <= candies[i+1]:
                        candies[i] = candies[i+1] + 1
        # print(candies)
        return sum(candies)
     