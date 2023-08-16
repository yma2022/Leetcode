# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = pre_right = pre_left = ListNode(next=head)
        right = left = head
        for i in range(k-1):
            pre_left = pre_left.next
            left = left.next

        null_checker = left

        while null_checker.next:
            pre_right = pre_right.next
            right = right.next
            null_checker = null_checker.next

        if left == right:
            return head

        pre_left.next, pre_right.next = right, left
        left.next, right.next = right.next, left.next
        return dummy.next 