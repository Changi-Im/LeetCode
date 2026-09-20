# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1_val = l1.val
        l2_val = l2.val
        
        k = 10
        while l1.next != None:
            l1 = l1.next
            l1_val += l1.val * k
            k *= 10
        
        k = 10
        while l2.next != None:
            l2 = l2.next
            l2_val += l2.val * k
            k *= 10
        
        print(l1_val, l2_val)
        ret_val = l1_val + l2_val
        ret = ListNode()
        cur = ret
        while ret_val > 0:
            cur.val = ret_val % 10
            ret_val /= 10
            if ret_val > 0:
                cur.next = ListNode()
                cur = cur.next
        
        return ret

