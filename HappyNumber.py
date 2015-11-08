class Solution(object):
    def trans(self,n):
        s = 0
        while n:
            s += (n%10)**2
            n /= 10
        return s
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = set()
        while True:
            new_n = self.trans(n)
            if new_n == 1:
                return True
            if new_n in l:
                return False
            l.add(new_n)
            n = new_n
