# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        curr = dummyHead
        while curr and curr.next:
            if curr.next.val == val:
                next = curr.next.next
                curr.next = next
            else:
                curr = curr.next
        return dummyHead.next
        