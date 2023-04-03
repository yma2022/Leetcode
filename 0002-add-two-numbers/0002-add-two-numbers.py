# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        if not l1 or not l2:
            return None
        head = ListNode()
        current = head
        carry = 0
        while l1 or l2:
            x, y = 0, 0
            if l1 != None:
                x = l1.val
            if l2 != None:
                y = l2.val
            current.next = ListNode(val=(x+y+carry)%10, next=None)
            current = current.next
            carry = (x + y + carry) // 10
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry > 0:
            current.next = ListNode(val=carry%10, next=None)
            
        return head.next
            