class Solution(object):
        def plusOne(self, digits):
                    """
        :type digits: List[int]
        :rtype: List[int]
        """
        t = len(digits) - 1
        while t >= 0:
            digits[t] = digits[t] + 1
            if digits[t] != 10:
                break
            digits[t] = 0
            t -= 1
        else:
            digits.insert(0,1)
        return digits
