# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, tail):
        prev = head
        curr = prev.next
        first = curr
        while curr != tail:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head.next = prev
        first.next = tail
        return first

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        curr = dummyHead
        tail = dummyHead.next
        index = 0
        while tail:
            index += 1
            if index % k == 0:
                curr = self.reverse(curr, tail.next)
                tail = curr.next
            else:
                tail = tail.next
        return dummyHead.next
                    
                
        