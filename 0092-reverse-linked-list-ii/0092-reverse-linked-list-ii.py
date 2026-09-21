# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        l = []
        idx = 1
        cur = head
        leftNode, rightNode = None, None
        while idx <= right + 1 and cur is not None: 
            if idx == left - 1:
                leftNode = cur
            if idx == right + 1:
                rightNode = cur

            if idx >= left and idx <= right:
                new = ListNode()
                new.val = cur.val
                l.append(new) 
            cur = cur.next
            idx += 1
        
        for i in range(len(l)-1, 0, -1):
            l[i].next = l[i-1]
        
        if rightNode is not None:
            l[0].next = rightNode
        if leftNode is not None:
            leftNode.next = l[-1]
            return head

        return l[-1]
        