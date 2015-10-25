class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            isMinus = True
            x = -x
        else:
            isMinus = False
        ret = 0
        while x:
            ret = ret*10 + x%10
            x /= 10
        if isMinus:
            ret = -ret
            
        return 0 if ret > 2147483647 or ret < -2147483648 else ret