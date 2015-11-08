class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        dupIndex = []
        for index,num in enumerate(nums):
            if num in num_set:
                dupIndex.append(index)
            num_set.add(num)
            
        dupIndex.reverse()
        for index in dupIndex:
            del nums[index]
            
        return len(nums)

