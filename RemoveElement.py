class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #nums = [num for num in nums if num != val]
        #return len(nums)
        countx=nums.count(val)
        for i in range(0,countx):
            nums.remove(val)
        return len(nums)
