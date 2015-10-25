class Solution(object):
    def getDigits(self,num):
        digits = []
        while(num):
            digits.append(num%10)
            num/=10
        return digits
        
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(num>=10):
            digits = self.getDigits(num)
            num = sum(digits)
        return num