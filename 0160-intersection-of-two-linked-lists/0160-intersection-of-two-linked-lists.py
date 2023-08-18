# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1 = headA
        curr2 = headB
        l1 = 0
        l2 = 0
        while curr1 or curr2:
            if curr1:
                l1 += 1
                curr1 = curr1.next
            if curr2:
                l2 += 1
                curr2 = curr2.next
        
        if l1 >= l2:
            fast = headA
            slow = headB
        else:
            fast = headB
            slow = headA
        
        k = abs(l1 - l2)
        
        while k:
            fast = fast.next
            k -= 1
            
        while fast != slow:
            fast = fast.next
            slow = slow.next
            
        
        return slow
            
        