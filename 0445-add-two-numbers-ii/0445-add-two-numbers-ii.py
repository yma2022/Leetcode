# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(head):
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        reversed_l1 = reverse_list(l1)
        reversed_l2 = reverse_list(l2)
        carry = 0
        dummyHead = ListNode()
        curr = dummyHead
        curr1, curr2 = reversed_l1, reversed_l2
        while curr1 or curr2:
            temp = ListNode()
            curr1_val = curr1.val if curr1 else 0
            curr2_val = curr2.val if curr2 else 0
            temp.val = (curr1_val + curr2_val + carry) % 10
            curr.next = temp
            curr = curr.next
            carry = (curr1_val + curr2_val + carry) // 10
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        if carry:
            curr.next = ListNode(val=carry)
        return reverse_list(dummyHead.next)
            
            
        