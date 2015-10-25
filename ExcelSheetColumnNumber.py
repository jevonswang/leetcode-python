class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for ch in list(s):
            ret = ret*26 + ord(ch) - ord('A') + 1
        return ret