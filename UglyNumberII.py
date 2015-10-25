class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = []
        factor2 = 1
        factor3 = 1
        factor5 = 1
        index2 = 0
        index3 = 0
        index5 = 0
        
        for i in xrange(n):
            minNum = min(factor2,factor3,factor5)
            ugly.append(minNum)
            if factor2 == minNum:
                factor2 = ugly[index2] * 2
                index2 += 1
            if factor3 == minNum:
                factor3 = ugly[index3] * 3
                index3 += 1
            if factor5 == minNum:
                factor5 = ugly[index5] * 5
                index5 += 1
        return ugly[-1]