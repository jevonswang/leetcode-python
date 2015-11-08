# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
        def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head;
        while p.next != None:
            q = p.next
            if p.val == q.val:
                p.next = q.next
                del q
            else:
                p = q
        return head
