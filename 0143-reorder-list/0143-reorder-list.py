# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def find_first_half_end(head):
            fast = head
            slow = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def reverse_list(head):
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        first_half_end = find_first_half_end(head)
        second_half = reverse_list(first_half_end.next)
        
        dummyHead = ListNode()
        first_half = head
        curr = dummyHead
        while second_half:
            curr.next  = first_half
            first_half = first_half.next
            curr = curr.next
            curr.next = second_half
            second_half = second_half.next
            curr = curr.next
        if first_half != first_half_end.next:
            curr.next = first_half_end
            curr = curr.next
            curr.next = None
        