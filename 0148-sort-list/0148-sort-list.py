# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getMid(head):
            prev = None
            while head and head.next:
                prev = head if prev == None else prev.next
                head = head.next.next
            mid = prev.next
            prev.next = None
            return mid
        
        def merge(list1, list2):
            dummyHead = ListNode()
            curr = dummyHead
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                    
                curr = curr.next
            if list1:
                curr.next = list1
            else:
                curr.next = list2
            return dummyHead.next
        if not head or not head.next:
            return head
        mid = getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)
        