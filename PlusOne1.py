class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(digit) for digit in digits]
        digits = int("".join(digits))
        digits += 1
        digits = list(str(digits))
        for i in range(len(digits)):
            digits[i] = int(digits[i])
        #digits = [int(digit) fot digit in digits]
        return digits
