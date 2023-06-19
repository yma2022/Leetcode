# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head

        curr = dummyHead
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                temp = curr.next
                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                curr.next = temp.next
            else:
                curr = curr.next
        return dummyHead.next