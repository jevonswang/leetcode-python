# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
        def mergeTwoLists(self, l1, l2):
                    """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        p1 = l1
        p2 = l2
        
        # get the first node
        if p1.val > p2.val:
            l3 = p2
            p2 = p2.next
        else:
            l3 = p1
            p1 = p1.next
        p3 = l3
        
        # merge the two list
        while p1 and p2:
            if p1.val > p2.val:
                p3.next = p2
                p3 = p3.next
                p2 = p2.next
            else:
                p3.next = p1
                p3 = p3.next
                p1 = p1.next
        
        # add the rest nodes to the end
        if p1:
            p3.next = p1
        if p2:
            p3.next = p2
        
        return l3
